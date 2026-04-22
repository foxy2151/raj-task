"""
TASK-3: AI Chatbot with NLP
Internship: CODTECH

Description:
This chatbot uses NLTK (Natural Language Toolkit) to process
user input and respond to queries using basic NLP techniques.
"""

import nltk
import random
import string

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required resources (first time only)
nltk.download('punkt')
nltk.download('wordnet')

# Initialize Lemmatizer
lemmatizer = WordNetLemmatizer()

# ==============================
# 🧠 KNOWLEDGE BASE
# ==============================
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm fine!", "Doing great!", "All good!"],
    "your name": ["I'm a chatbot.", "You can call me AI Bot."],
    "course": ["This is CODTECH Internship."],
    "python": ["Python is a powerful programming language."],
    "bye": ["Goodbye!", "See you later!", "Bye!"]
}

# ==============================
# 🔍 PREPROCESS TEXT
# ==============================
def preprocess(text):
    """Lowercase + tokenize + lemmatize"""
    text = text.lower()
    tokens = word_tokenize(text)

    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]

    return tokens

# ==============================
# 🤖 CHATBOT RESPONSE LOGIC
# ==============================
def get_response(user_input):
    tokens = preprocess(user_input)

    for key in responses:
        key_tokens = preprocess(key)

        if set(key_tokens).issubset(set(tokens)):
            return random.choice(responses[key])

    return "Sorry, I don't understand that."

# ==============================
# 🚀 MAIN CHAT LOOP
# ==============================
def chatbot():
    print("🤖 Chatbot Started! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Bot:", random.choice(responses["bye"]))
            break

        response = get_response(user_input)
        print("Bot:", response)

# ==============================
# ▶️ RUN
# ==============================
if __name__ == "__main__":
    chatbot()
