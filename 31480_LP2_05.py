import os
import nltk
import random
import shutil
from nltk.stem import WordNetLemmatizer
from termcolor import colored

terminal_width = shutil.get_terminal_size().columns


def clear_terminal():
    os_name = os.name
    if os_name == "nt":
        os.system("cls")
    elif os_name == "posix":
        os.system("clear")


nltk.download("punkt")
nltk.download("wordnet")
nltk.download("stopwords")

lemmatizer = WordNetLemmatizer()
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
        "lolololololol, bro is suffering from skill issues",
    ],
    "favorite": [
        "I don't have a favorite, but I love all topics!",
        "My favorite thing is helping you, lol jk",
        "I love shit talking to people!",
    ],
}

patterns = {
    "greeting": ["hi", "hello", "hey", "greetings", "howdy"],
    "goodbye": ["bye", "goodbye", "see you", "later"],
    "thanks": ["thanks", "thank you"],
    "how_are_you": [
        "how are you",
        "how's it going",
        "how do you do",
        "how are you doing",
    ],
    "weather": [
        "what's the weather",
        "tell me the weather",
        "how's the weather",
        "is it raining",
    ],
    "name": ["what's your name", "who are you", "tell me your name", "who are you?"],
    "joke": ["tell me a joke", "make me laugh", "tell me something funny"],
    "help": ["help", "can you help", "assist me", "i need help", "can you assist"],
    "favorite": [
        "what's your favorite",
        "what do you like",
        "tell me your favorite thing",
        "what's your favorite thing",
    ],
}


def match_intent(user_input):
    processed_input = preprocess_input(user_input)
    for intent, keywords in patterns.items():
        for keyword in keywords:
            if processed_input == keyword or keyword in processed_input:
                return intent
    return None


def preprocess_input(user_input):
    user_input = user_input.lower().strip()
    return user_input


def chatbot_response(user_input):
    intent = match_intent(user_input)
    if intent:
        return random.choice(responses[intent])
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"


def run_chatbot():
    clear_terminal()
    print(colored("\y0y: ", "green", attrs=["bold"]), end="")
    print("Hello! How can I assist you today?")
    print()

    while True:
        print(colored("You: ", "blue", attrs=["bold"]), end="")
        user_input = input()

        if user_input.lower() == "bye":
            print(colored("y0y: ", "green", attrs=["bold"]), end="")
            print("Goodbye! See you next time!")
            break

        response = chatbot_response(user_input)
        print(colored("y0y: ", "green", attrs=["bold"]), end="")
        print(response)
        print()


if __name__ == "__main__":
    run_chatbot()
