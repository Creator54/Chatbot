#!/usr/bin/env python3

import os, sys, random, dialogs, help

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def start():
    greetings = [ "Hi, there I am a chatbot !", "Welcome back !", "Greetings, Human !", "Hey, good to see you :)", "Hello Amigo !", "How may i help ?" ]
    print(random.choice(greetings) + "\n")
    user_input = input("You: ")
    while user_input != "exit":
        if user_input == "clear":
            clear()
            user_input = input("You: ")
        elif user_input == "help":
            help.fn()
            user_input = input("You: ")
        else:
            print("Bot: " + dialogs.reply(user_input) + "\n")
            user_input = input("You: ")

if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] == "start":
        start()
    else:
        help.fn()
