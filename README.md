# Chatbot
This is a simple chatbot program written in Python using the Natural Language Toolkit (NLTK) library for natural language processing. The chatbot uses a dictionary to store pre-defined responses based on certain keywords in the user's input.

# Installation
To use this chatbot, you'll need to have Python 3 installed on your system. You'll also need to install the NLTK library. 
You can do this using pip: pip install nltk

After installing NLTK, you'll need to download some data for tokenizing and lemmatizing text. 
In your Python script, add the following code: 
import nltk
nltk.download('punkt')
nltk.download('wordnet')

# Usage
To run the chatbot, save the script as a .py file and run it in your terminal:
python chatbot.py

The chatbot will prompt you for input, and respond based on the pre-defined responses or a default response if no keywords are found.

#Customization
To customize the chatbot, you can modify the pre-defined responses in the responses dictionary. You can also modify the keywords used to trigger these responses. Additionally, you can add more complex natural language processing features using NLTK or other libraries.
