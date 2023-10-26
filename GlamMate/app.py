# Import necessary libraries
from keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
from nltk.tokenize import word_tokenize
import nltk

import mysql.connector  # Import the database connector library

# Download NLTK data
nltk.download('punkt')
nltk.download("stopwords")
nltk.download('wordnet')

# Load intents data from a JSON file
intents = json.loads(open('intents.json').read())
# Load preprocessed data from pickle files
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

# Function to establish a database connection
def establish_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345678',
            database='chatbotdb'
        )
        return connection
    except Exception as e:
        print(f"Database connection error: {str(e)}")
        return None

# Define a function to clean up a sentence for processing
def clean_up_sentence(sentence):
    # Tokenize the pattern - split words into an array
    sentence_words = nltk.word_tokenize(sentence)
    # Lemmatize each word - create a short form for the word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
# Define a function to convert a sentence to a "bag of words" representation
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def get_order_by_id(order_id, db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM orders WHERE idorders = %s", (order_id,))
    order_data = cursor.fetchone()
    cursor.close()

    if order_data:
        return f"Here's your Order ->\n  Order ID: {order_data[0]}\n  Date: {order_data[1]}\n  Amount: {order_data[2]}\n  Shipping Address:{order_data[3]}\n  Order Status: {order_data[4]}\n  Order Details: {order_data[5]} "
    else:
        return "Order not found."

# Define a function to get a response based on the predicted intent
def getResponse(intents, intents_json, db_connection):
    tag = intents[0]['intent']
    list_of_intents = intents_json['intents']
    for intent in list_of_intents:
        if intent['tag'] == tag:
            responses = intent['responses']
            if tag == 'order_status':
                order_id = intents[0]['order_id']
                response = get_order_by_id(order_id, db_connection)
                return response
            else:
                return random.choice(responses)

    return "I'm sorry, I don't understand that."

# Define a function to get a chatbot response(chatbot logic)
def chatbot_response(text, db_connection):
    if text.startswith("get order by ID"):
        order_id = text.split()[-1]
        order_data = get_order_by_id(order_id, db_connection)
        return order_data
    else:
        return predict_class(text, db_connection)

# Define a function to predict the intent of a sentence using the model
def predict_class(sentence, db_connection):
    # filter out predictions below a threshold
    p = bag_of_words(sentence)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    response = getResponse(return_list, intents, db_connection)
    return response

"""
GUI Interface
"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def chat():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    db_connection = establish_db_connection()
    # Implement your chatbot_response function here and get a response
    response = chatbot_response(message,db_connection)

    return response
