
import random

greeting = {
    "hello": [
        "Hello, how are you?",
        "Hey! What's up?",
        "Hello! Nice to meet you.",
        "Hi there! How's your day?"
    ],

    "hi": [
        "Hello!",
        "Hey!",
        "Hi, how are you?",
        "Hey buddy!",
        "Good to see you!"
    ]
}

greet = input("Please enter: ").lower()

if greet in greeting:
    print(random.choice(greeting[greet]))

else:
    print("Sorry! I don't understand.")

