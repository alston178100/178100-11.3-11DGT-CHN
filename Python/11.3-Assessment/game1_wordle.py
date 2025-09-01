""""Python code for game 1: Wordle."""

import random

f = open(r"Python\11.3-Assessment\wordle_word_list.txt")
word = f.readlines()
for i in range(len(word)):
    word[i] = word[i].strip()

print(word[random.randint(0, len(word) - 1)])


