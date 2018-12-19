# by Jason Basden


import random
import string


def getLetter():
    return random.choice(string.ascii_lowercase)

def getNumber():
    return random.choice(string.digits)

def getCLetter():
    return random.choice(string.ascii_uppercase)

def getPunctuation():
    return random.choice(string.punctuation)

def getRandom():
    my_list = [getLetter, getNumber, getCLetter, getPunctuation]
    return random.choice(my_list)()


password = ''
for num in range(0, 15):
    password = password + getRandom()        

print(password)
    
"""
() calling function
0 is included
15 in not included
"""
