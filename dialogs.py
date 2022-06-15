import random, re

def reply(user_input=""):
    if user_input == "" or len(user_input)< 8 and not re.match("hello",user_input, flags=re.I) and not re.match("hi",user_input, flags=re.I):
        replies = [ "Hi, I don't understand could you please elaborate ?", "Sorry did't got you !", "Use more words please !", "Can we talk a bit more ?" ]
        return random.choice(replies)
    else:
        return user_input

