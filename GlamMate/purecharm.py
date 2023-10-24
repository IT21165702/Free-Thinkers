import tkinter as tk
import mysql.connector
from keras.models import load_model
import json
import random
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

# Load the chatbot model and related data
model = load_model('chatbot_model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))

# Function to clean up user input
def clean_up_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# Function to create a bag of words
def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)

# Function to predict user intent
def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

# Function to get a response from intents JSON
def get_response(intents, tag):
    for intent in intents:
        if intent['tag'] == tag:
            responses = intent['responses']
            return random.choice(responses)
    return "I'm sorry, I don't understand that."

# Function to handle user input
def chatbot_response(user_input):
    intents = predict_class(user_input, model)
    intent = intents[0]['intent']
    response = get_response(intents, intent)
    return response

#       ? ????????
# Function to send a message
def send_message(event=None):
    user_input = entry_box.get()
    entry_box.delete(0, tk.END)
    if user_input.strip() != '':
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, "You: " + user_input + '\n\n')
        chat_log.config(foreground="#000000", font=("Verdana", 12))

        bot_response = chatbot_response(user_input)
        chat_log.insert(tk.END, "Bot: " + bot_response + '\n\n')

        chat_log.config(state=tk.DISABLED)
        chat_log.yview(tk.END)

# Create a MySQL database connection
#user = "your_username"
#password = "your_password"
#host = "your_mysql_host"
#database = "your_database_name"

#connection = mysql.connector.connect(
#    user=user,
#    password=password,
#    host=host,
#    database=database
#)

# Create the main GUI window
root = tk.Tk()
root.title("E-Commerce Chatbot")
root.geometry("800x800")

# Create chat log
chat_log = tk.Text(root, bd=0, bg="#c5f0e3", fg="#000000", font=("Helvetica 13 bold"))
chat_log.config(state=tk.DISABLED)
chat_log.pack(fill=tk.BOTH, expand=True)

# Create user input field
entry_box = tk.Entry(root, bg="white", font=("Arial", 12))
entry_box.bind("<Return>", send_message)
entry_box.pack(fill=tk.BOTH, padx=5, pady=5)

# Create send button
send_button = tk.Button(root, text="Send", command=send_message, font=("Verdana", 12, 'bold'), bg="#ed9061",
                        activebackground="#3c9d9b", fg='#ffffff')
send_button.pack(fill=tk.BOTH)

# Start the GUI event loop
root.mainloop()

# Close the MySQL database connection when done
connection.close()
