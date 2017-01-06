from random import randint
from time import sleep
name = ['Neha', 'Lee', 'Sam', 'Leo', 'Mom', 'Dad']
verb = ['buys', 'rides', 'kicks']
noun = ['lion', 'bicycle', 'plane', 'mom', 'dad']
def pick(words):
    num_words = len(words)
    num_picked = randint(0, num_words - 1)
    word_picked = words[num_picked]
    return word_picked
while True:
    print(pick(name), pick(verb), 'a', pick(noun), end='.\n')
    sleep(0.05)
