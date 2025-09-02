""""Python code for game 1: Wordle."""

import random

f = open(r"Python\11.3-Assessment\wordle_word_list.txt")
word = f.readlines()
for i in range(len(word)):
    word[i] = word[i].strip()

target_word = word[random.randint(0, len(word) - 1)]
print(target_word)

user_word = ""
attempts = 0
guessed = False

while attempts < 6:
    letter_inp = letter_inp = input("Enter letter: ")
    while letter_inp != "]":
        if letter_inp == "[":
            if len(user_word) >= 1:
                user_word = user_word[:-1]
            else:
                print("No letters")
        else:
            if len(user_word) < 5:
                user_word += letter_inp
            else:
                print("Too many letters")
        print(user_word)
        letter_inp = input("Enter letter: ")
    
    if len(user_word) != 5:
        print("Entered but not enough letters")
    elif user_word not in word:
        print("Invalid word")
    else:
        attempts += 1
    
        if user_word == target_word:
            print(target_word)
            print("Correct word")
            break
        else:
            cond = ""
            for i in range(5):
                if user_word[i] == target_word[i]:
                    cond += "2"
                elif user_word[i] in target_word:
                    cond += "1"
                else:
                    cond += "0"
            print(user_word)
            print(cond)
            print("Not the word")
        user_word = ""

print(attempts)
