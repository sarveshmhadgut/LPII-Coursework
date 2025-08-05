import os
import re
import nltk
import random
from termcolor import colored
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

patterns = {
    "greeting": [r"\bhi\b", r"\bhello\b", r"\bhey\b", r"\bgreetings\b", r"\bhowdy\b"],
    "goodbye": [
        r"\bbye\b",
        r"\bgoodbye\b",
        r"\blater\b",
        r"\bsee you\b",
        r"\bsee ya\b",
        r"\badios\b",
    ],
    "thanks": [r"\bthanks\b", r"\bthank you\b", r"\bappreciated\b"],
    "weather": [r"\bweather\b", r"\bsunny\b", r"\brain(ing)?\b", r"\bforecast\b"],
    "name": [r"\bwhat('?s| is) your name\b", r"\bwho are you\b", r"\byour name\b"],
    "joke": [r"\bjoke\b", r"\blaugh\b", r"\bfunny\b", r"\bmood\b"],
    "help": [r"\bhelp\b", r"\bassist\b", r"\bassistance\b", r"\bcan you help\b"],
    "favorite": [r"\bfavorite\b", r"\bdo you like\b", r"\bpreference\b"],
}

responses = {
    "greeting": ["Hello!", "Hi there!", "Greetings!", "Hey!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "thanks": ["You're welcome!", "Happy to help!", "Anytime!"],
    "how_are_you": [
        "I'm good, thanks!",
        "I'm doing well!",
        "I'm great, thanks for asking!",
        "Shut up! dweeb",
    ],
    "weather": [
        "It's sunny today.",
        "It looks like it's going to rain.",
        "I think the weather is perfect today!",
        "Look outside buddy, touch some grass",
    ],
    "name": [
        "Hello! Master Chief, it's me y0y.",
        "You can call me y0y!",
        "I don't have a name, but you can call me anything you like.",
    ],
    "joke": [
        "Why don't skeletons fight each other? They don't have the guts!",
        "I told my computer I needed a break, now it won't stop sending me Kit-Kats.",
        "Why don't oysters share their pearls? Because they're shellfish!",
        "You tell me, you are the clown",
    ],
    "help": [
        "I'm here to help you! What do you need assistance with?",
        "Sure, what can I assist you with today?",
        "I'm here to answer your questions. How can I help?",
        "hell na!, go figure it out yourself",
        "bro is suffering from skill issues",
    ],
    "favorite": [
        "I don't have a favorite, but I love all topics!",
        "My favorite thing is helping you, lol jk",
        "I love shit talking to people!",
    ],
}


def preprocess(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [
        token for token in tokens if token not in stop_words and token.isalnum()
    ]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    return " ".join(lemmatized_tokens)


def get_intent(user_input):
    cleaned_text = preprocess(user_input)
    for intent, pattern_list in patterns.items():
        for pattern in pattern_list:
            if re.search(pattern, cleaned_text):
                return intent
    return None


def run_chatbot():
    print(colored("\nChatbot:", "green", attrs=["bold"]), end=" ")
    print("Hello! How can I assist you today?")

    while True:
        print(colored("\nYou:", "blue", attrs=["bold"]), end=" ")
        query = input()

        intent = get_intent(query)
        if intent:
            print(colored("Chatbot:", "green", attrs=["bold"]), end=" ")
            print(random.choice(responses[intent]))
        else:
            print(
                colored("Chatbot:", "green", attrs=["bold"]),
                "Sorry, I didn't understand that. Can you rephrase?",
            )
        if intent == "goodbye":
            break


if __name__ == "__main__":
    os.system("clear")
    run_chatbot()
