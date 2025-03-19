import random

def pickWord():
    with open('SOWPODS dic.txt', 'r') as f:
        words = f.readlines()
    return random.choice(words).strip()


print(pickWord())