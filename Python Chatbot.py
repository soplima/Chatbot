import nltk
from nltk.stem import WordNetLemmatizer

# download necessary data
nltk.download('punkt')
nltk.download('wordnet')

# initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# define some responses
responses = {
    "hello": "Hi there!",
    "what's your name?": "My name is Chatbot!",
    "how are you?": "I'm doing well, thank you.",
    "bye": "Goodbye!"
}

# define a function to process user input and return a response
def process_input(input_text):
    # tokenize the input text
    words = nltk.word_tokenize(input_text.lower())
    # lemmatize the words
    words = [lemmatizer.lemmatize(word) for word in words]
    # check if any keywords in responses are in the input
    for key_word in responses.keys():
        if key_word in words:
            return responses[key_word]
    # if no keywords found, return a default response
    return "I'm sorry, I don't understand. Can you please rephrase?"

# loop to continually prompt user for input and respond
while True:
    user_input = input("You: ")
    response = process_input(user_input)
    print("Chatbot:", response)
