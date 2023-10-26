

# # Download necessary NLTK data
# nltk.download('punkt')
# nltk.download("stopwords")
# nltk.download('wordnet')

# # Load the pre-trained chatbot model
# model = load_model('chatbot_model.h5')

# # Load intents data from a JSON file
# intents = json.loads(open('intents.json').read())

# # Load preprocessed data from pickle files
# words = pickle.load(open('words.pkl','rb'))
# classes = pickle.load(open('classes.pkl','rb'))

# # Function to establish a database connection
# def establish_db_connection():
#     try:
#         connection = mysql.connector.connect(
#             host='localhost',
#             user='root',
#             password='12345678',
#             database='chatbotdb'
#         )
#         return connection
#     except Exception as e:
#         print(f"Database connection error: {str(e)}")
#         return None

# # Define a function to clean up a sentence for processing
# def clean_up_sentence(sentence):
#     # Tokenize the pattern - split words into an array
#     sentence_words = nltk.word_tokenize(sentence)
#     # Lemmatize each word - create a short form for the word
#     sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
#     return sentence_words

# # Return a bag of words array: 0 or 1 for each word in the bag that exists in the sentence
# # Define a function to convert a sentence to a "bag of words" representation
# def bag_of_words(sentence):
#     sentence_words = clean_up_sentence(sentence)
#     bag = [0] * len(words)
#     for w in sentence_words:
#         for i, word in enumerate(words):
#             if word == w:
#                 bag[i] = 1
#     return np.array(bag)

# # Define a function to extract an order ID from user input
# def extract_order_id(user_input):
#     order_id_pattern = r'O\d{3,}'  # Matches sequences of four or more digits

#     # Search for the order ID pattern in the user's input
#     match = re.search(order_id_pattern, user_input)

#     if match:
#         order_id = match.group(0)  # The first match is considered the order ID
#         return order_id
#     else:
#         return None  # Return None if no order ID is found in the input

# # Define a function to extract a product ID from user input
# def extract_product_id(user_input):
#     product_id_pattern = r'P\d{3,}'  # Matches sequences of four or more digits

#     # Search for the product ID pattern in the user's input
#     match = re.search(product_id_pattern, user_input)

#     if match:
#         product_id = match.group(0)  # The first match is considered the product ID
#         return product_id
#     else:
#         return None  # Return None if no product ID is found in the input

# # Define a function to get order details by ID
# def get_order_by_id(order_id, db_connection):
#     cursor = db_connection.cursor()
#     cursor.execute("SELECT * FROM orders WHERE idorders = %s", (order_id,))
#     order_data = cursor.fetchone()
#     cursor.close()

#     if order_data:
#         return f"Here's your Order ->\n  Order ID: {order_data[0]}\n  Date: {order_data[1]}\n  Amount: {order_data[2]}\n  Shipping Address: {order_data[3]}\n  Order Status: {order_data[4]}\n  Order Details: {order_data[5]}"
#     else:
#         return "Order not found."

# # Define a function to get product details by ID
# def get_products(product_id, db_connection):
#     cursor = db_connection.cursor()
#     cursor.execute("select product_name, description, price from products where idproducts = %s", (product_id,))
#     product_data = cursor.fetchone()
#     cursor.close()

#     if product_data:
#         return f"Product Details ->\n  Product Name: {product_data[0]}\n  Description: {product_data[1]}\n  Price: {product_data[2]}"
#     else:
#         return "Product not found."

# # Define a function to get product promotions
# def get_product_promotions(product_id, db_connection):
#     cursor = db_connection.cursor()
#     cursor.execute("SELECT p.product_name, p.price, pr.discount_value FROM products p INNER JOIN promotions pr ON p.idproducts = pr.productID WHERE p.product_name = 'Your_Product_Name", (product_id,))
#     promotion = cursor.fetchone()
#     cursor.close()

#     if promotion:
#         return f"Here's the Promotions Available for the Product ->\n  Product Name: {promotion[0]}\n  Price: {promotion[1]}\n  Discount: {promotion[2]}"
#     else:
#         return "Product not found."
    
# # Define a function to get category products
# def get_category_products(catergories_name, db_connection):
#     cursor = db_connection.cursor()
#     cursor.execute("SELECT p.product_name, p.price FROM products p INNER JOIN categories c ON p.categoryID = c.idcategories WHERE c.catergories_name = %s", (catergories_name,))
#     category_products = cursor.fetchone()
#     cursor.close()

#     if category_products:
#         return f"Product under {catergories_name} category ->\n  Product Name: {category_products[0]}\n Price: {category_products[1]}"
#     else:
#         return "Category not found."



# Import necessary libraries
from keras.models import load_model
# Load the pre-trained chatbot model
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

import re

def extract_order_id(user_input):
    # Regular expression to find a sequence of digits that may represent an order ID
    #order_id_pattern = r'\d+'
    order_id_pattern = r'O\d{3,}'  # Matches sequences of four or more digits

    # Search for the order ID pattern in the user's input
    match = re.search(order_id_pattern, user_input)

    if match:
        order_id = match.group(0)  # The first match is considered the order ID
        return order_id
    else:
        return None  # Return None if no order ID is found in the input
    
def extract_product_id(user_input):
    # Regular expression to find a sequence of digits that may represent an order ID
    #order_id_pattern = r'\d+'
    product_id_pattern = r'P\d{3,}'  # Matches sequences of four or more digits

    # Search for the order ID pattern in the user's input
    match = re.search(product_id_pattern, user_input)

    if match:
        product_id = match.group(0)  # The first match is considered the order ID
        return product_id
    else:
        return None  # Return None if no order ID is found in the input

def get_order_by_id(order_id, db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM orders WHERE idorders = %s", (order_id,))
    order_data = cursor.fetchone()
    cursor.close()

    if order_data:
        return f"Here's your Order ->\n  Order ID: {order_data[0]}\n  Date: {order_data[1]}\n  Amount: {order_data[2]}\n  Shipping Address:{order_data[3]}\n  Order Status: {order_data[4]}\n  Order Details: {order_data[5]} "
    else:
        return "Order not found."

def get_products(product_id, db_connection):
    cursor = db_connection.cursor()
    cursor.execute("select product_name,description,price from products where idproducts = %s", (product_id,))
    product_data = cursor.fetchone()
    cursor.close()

    if product_data:
        return f"Product Details ->\n  Product Name: {product_data[0]}\n  Description: {product_data[1]}\n  Price: {product_data[2]}\n "
    else:
        return "Product not found."

# def get_categories(product_id, db_connection):
#     cursor = db_connection.cursor()
#     cursor.execute("select * from categories", (product_id,))
#     product_data = cursor.fetchone()
#     cursor.close()

#     if product_data:
#         return f"Here's your Order ->\n  Product Name: {product_data[0]}\n  Description: {product_data[1]}\n  Price: {product_data[2]}\n "
#     else:
#         return "Product not found."

def get_product_promotions(product_id, db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT p.product_name, p.price, pr.discount_value FROM products p INNER JOIN promotions pr ON p.idproducts = pr.productID WHERE p.product_name = %s", (product_id,))
    promotion = cursor.fetchone()
    cursor.close()

    if promotion:
        return f"Here's the Promotions Available for the Product ->\n  Product Name: {promotion[0]}\n  Price: {promotion[1]}\n  Discount: {promotion[2]}\n "
    else:
        return "No discounts."
    
# Define a function to get category products    
def get_category_products(catergories_name, db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT p.product_name, p.price FROM products p INNER JOIN categories c ON p.categoryID = c.idcategories WHERE c.catergories_name = '%s'", (catergories_name,))
    category_products = cursor.fetchone()
    cursor.close()

    if category_products:
        return f"Product under catergories_name category->\n  Product Name: {category_products[0]}\n Price: {category_products[1]}\n "
    else:
        return "Not Available."    

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

    # If no suitable response is found, return a default message
    default_responses = intents_json['default_responses']
    return random.choice(default_responses)

    return "I'm sorry, I don't understand that."

# Define a function to get a chatbot response(chatbot logic)
def chatbot_response(text, db_connection):
    order_id = extract_order_id(text)
    product_id = extract_product_id(text)
    if order_id:
        order_data = get_order_by_id(order_id, db_connection)
        return order_data
    if text.startswith("Find me"):
        catergories_name = text.split()[-1]
        category_products = get_category_products(catergories_name, db_connection)
        return category_products
    if product_id:
        product_data = get_products(product_id, db_connection)
        return product_data
    # if text.startswith("Product"):
    #     product_id = text.split()[-1]
    #     product_data = get_products(product_id, db_connection)
    #     return product_data
    if text.startswith("Discount for"):
        product_id = text.split()[-1]
        product_data = get_product_promotions(product_id, db_connection)
        return product_data
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



# """
# GUI Interface
# """  

import tkinter as tk
from PIL import Image, ImageTk

# Define color constants
BG_COLOR = "#cdc3de"
TEXT_COLOR = "#333333"
FONT = "Courier 14"
FONT_BOLD = "Courier 13 bold"
MAIN_BG_COLOR = "#949199"
ACCENT_COLOR = "#775ba8"
TRANS_COLOR = 'rgba(255, 255, 255, 0.5)'  # Set the background color with transparency


# Define the send function
def send():
    # Establish a database connection
    db_connection = establish_db_connection()
    
    # Get the message from the entry box
    msg = entry_box.get()
    entry_box.delete(0, tk.END)
    
    if msg.strip() != '':
        # Set a fixed character limit for each line and wrap text by words
        chat_log.config(wrap=tk.WORD)
        
        # Load and resize the avatar image
        your_image = Image.open("avatar.jpg")
        your_image.thumbnail((50, 50))
        your_image = ImageTk.PhotoImage(your_image)
        
        # Define a 'bold' tag for bold text
        chat_log.tag_configure('bold', font=("Verdana", 12, 'bold'))

        # Enable chat log for editing
        chat_log.config(state=tk.NORMAL)
        
        # Insert the user's message
        chat_log.insert(tk.END, msg, 'user')
        
        # Apply 'bold' tag to the "You" label
        chat_log.insert(tk.END, "  : You", 'bold')
        
        # Insert the user's avatar image
        chat_log.image_create('end', image=your_image)
        
        # Add space
        chat_log.insert(tk.END, " \n", 'spacing')
        
        # Set text color and font
        chat_log.config(foreground="#222222", font=("Verdana", 12))

        # Add space
        chat_log.insert(tk.END, " \n", 'spacing')
        
        # Get the chatbot's response
        res = chatbot_response(msg, db_connection)
        
        # Apply 'bold' tag to the "Bot" label
        chat_log.insert(tk.END, "  Bot:  ", 'bold')
        
        # Add 'bot' tag for the chatbot's response
        chat_log.insert(tk.END, res + ' \n', 'bot')
        
        # Add space
        chat_log.insert(tk.END, " \n", 'spacing')
        
        # Disable chat log for viewing
        chat_log.config(state=tk.DISABLED)
        
        # Scroll to the end of the chat log
        chat_log.yview(tk.END)

        
        # Close the database connection
        db_connection.close()

# Create the main application window
base = tk.Tk()
base.title("GlamMate Chatbot")
base.geometry("800x600")

# Load and display the background image
bg_image = Image.open("fg.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(base, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Create the top frame with the avatar and chatbot label
top_frame = tk.Frame(base, bg=BG_COLOR)
top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=160, pady=10)

# Load and display the bot's avatar image
avatar_image = Image.open("avatar.jpg")
avatar_image.thumbnail((60, 60))
avatar_photo = ImageTk.PhotoImage(avatar_image)

bot_avatar_label = tk.Label(top_frame, image=avatar_photo, bg=BG_COLOR)
bot_avatar_label.image = avatar_photo
bot_avatar_label.pack(side=tk.LEFT, padx=(0, 20), pady=0)

# Create the chatbot's welcome label 
head_label = tk.Label(top_frame, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to GlamMate Chatbot", font=("Palatino 18 bold"), pady=10)
head_label.pack(side=tk.LEFT)

# Create the middle frame for the chat log
middle_frame = tk.Frame(base,bg="#97a7b0")
middle_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=80, pady=0)

# Create the chat log with a scrollbar
chat_log = tk.Text(middle_frame, bd=0,bg="#d3e4ed", fg=TEXT_COLOR, font=("Lato", 12))
chat_log.config(state=tk.DISABLED)
chat_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=0)

scrollbar = tk.Scrollbar(middle_frame, command=chat_log.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_log.config(yscrollcommand=scrollbar.set)

# Configure tags for user, bot, and spacing
chat_log.tag_configure('user', justify='right', lmargin1=25, lmargin2=25, rmargin=25, font=("Arial 13 "))
chat_log.tag_configure('bot', justify='left', lmargin1=25, lmargin2=25, rmargin=25, font=("Arial 13 "))
chat_log.tag_configure('spacing', spacing1=1)

# Create the bottom frame with an input box and send button
bottom_frame = tk.Frame(base)
bottom_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=30, pady=10)

entry_box = tk.Entry(bottom_frame, bg="white", font=("Arial", 18), width=40,)
entry_box.bind("<Return>", lambda event=None: send())
entry_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=10)

send_button = tk.Button(bottom_frame, text="Send", command=send, font=("Courier", 16, 'bold'), bg=ACCENT_COLOR, fg='white')
send_button.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Start the main event loop
base.mainloop()


# import tkinter as tk
# from PIL import Image, ImageTk

# # Define color constants
# BG_COLOR = "#cdc3de"
# TEXT_COLOR = "#333333"
# FONT = "Arial 14"
# FONT_BOLD = "Arial 13 bold"
# MAIN_BG_COLOR = "#949199"
# ACCENT_COLOR = "#775ba8"
# TRANS_COLOR = 'rgba(255, 255, 255, 0.5)'  # Set the background color with transparency


# # Define the send function
# def send():
#     # Establish a database connection
#     db_connection = establish_db_connection()
    
#     # Get the message from the entry box
#     msg = entry_box.get()
#     entry_box.delete(0, tk.END)
    
#     if msg.strip() != '':
#         # Set a fixed character limit for each line and wrap text by words
#         chat_log.config(wrap=tk.WORD)
        
#         # Load and resize the avatar image
#         your_image = Image.open("avatar.jpg")
#         your_image.thumbnail((50, 50))
#         your_image = ImageTk.PhotoImage(your_image)
        
#         # Define a 'bold' tag for bold text
#         chat_log.tag_configure('bold', font=("Verdana", 12, 'bold'))

#         # Enable chat log for editing
#         chat_log.config(state=tk.NORMAL)
        
#         # Insert the user's message
#         chat_log.insert(tk.END, msg, 'user')
        
#         # Apply 'bold' tag to the "You" label
#         chat_log.insert(tk.END, "  : You", 'bold')
        
#         # Insert the user's avatar image
#         chat_log.image_create('end', image=your_image)
        
#         # Add space
#         chat_log.insert(tk.END, " \n", 'spacing')
        
#         # Set text color and font
#         chat_log.config(foreground="#222222", font=("Verdana", 12))

#         # Add space
#         chat_log.insert(tk.END, " \n", 'spacing')
        
#         # Get the chatbot's response
#         res = chatbot_response(msg, db_connection)
        
#         # Apply 'bold' tag to the "Bot" label
#         chat_log.insert(tk.END, "  Bot:  ", 'bold')
        
#         # Add 'bot' tag for the chatbot's response
#         chat_log.insert(tk.END, res + ' \n', 'bot')
        
#         # Add space
#         chat_log.insert(tk.END, " \n", 'spacing')
        
#         # Disable chat log for viewing
#         chat_log.config(state=tk.DISABLED)
        
#         # Scroll to the end of the chat log
#         chat_log.yview(tk.END)

        
#         # Close the database connection
#         db_connection.close()

# # Create the main application window
# base = tk.Tk()
# base.title("GlamMate Chatbot")
# base.geometry("800x600")

# # Load and display the background image
# bg_image = Image.open("fg.jpg")
# bg_photo = ImageTk.PhotoImage(bg_image)
# bg_label = tk.Label(base, image=bg_photo)
# bg_label.place(relwidth=1, relheight=1)

# # Create the top frame with the avatar and chatbot label
# top_frame = tk.Frame(base, bg=BG_COLOR)
# top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=160, pady=10)

# # Load and display the bot's avatar image
# avatar_image = Image.open("avatar.jpg")
# avatar_image.thumbnail((60, 60))
# avatar_photo = ImageTk.PhotoImage(avatar_image)

# bot_avatar_label = tk.Label(top_frame, image=avatar_photo, bg=BG_COLOR)
# bot_avatar_label.image = avatar_photo
# bot_avatar_label.pack(side=tk.LEFT, padx=(0, 20), pady=0)

# # Create the chatbot's welcome label with "Arial" font
# head_label = tk.Label(top_frame, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome to GlamMate Chatbot", font=("Cavolini 20 bold"), pady=10)
# head_label.pack(side=tk.LEFT)

# # Create the middle frame for the chat log
# middle_frame = tk.Frame(base,bg="#97a7b0")
# middle_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=80, pady=0)

# # Create the chat log with a scrollbar
# chat_log = tk.Text(middle_frame, bd=0,bg="#d3e4ed", fg=TEXT_COLOR, font=("Lato", 12))
# chat_log.config(state=tk.DISABLED)
# chat_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=0)

# scrollbar = tk.Scrollbar(middle_frame, command=chat_log.yview)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# chat_log.config(yscrollcommand=scrollbar.set)

# # Configure tags for user, bot, and spacing
# chat_log.tag_configure('user', justify='right', lmargin1=25, lmargin2=25, rmargin=25)
# chat_log.tag_configure('bot', justify='left', lmargin1=25, lmargin2=25, rmargin=25)
# chat_log.tag_configure('spacing', spacing1=1)

# # Create the bottom frame with an input box and send button
# bottom_frame = tk.Frame(base)
# bottom_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=30, pady=10)

# entry_box = tk.Entry(bottom_frame, bg="white", font=("Lato", 18), width=40)
# entry_box.bind("<Return>", lambda event=None: send())
# entry_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# send_button = tk.Button(bottom_frame, text="Send", command=send, font=("Lato", 16, 'bold'), bg=ACCENT_COLOR, fg='white')
# send_button.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# # Start the main event loop
# base.mainloop()