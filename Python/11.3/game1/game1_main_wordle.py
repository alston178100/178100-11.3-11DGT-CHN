"""Tkinter code for of game 1: Wordle"""

from tkinter import *
import random
import subprocess
import csv

# Setting up user inputs

f = open(r"Python\11.3\txt_files\wordle_word_list.txt")
word_li = f.readlines()
for i in range(len(word_li)):
    word_li[i] = word_li[i].strip().upper()

target_word = word_li[random.randint(0, len(word_li) - 1)]
print(target_word)

f = open(r"Python\11.3\txt_files\user_word_list.txt")
user_word_li = f.readlines()
for i in range(len(user_word_li)):
    user_word_li[i] = user_word_li[i].strip().upper()

g_root = Tk(screenName="Game 1")
g_root.title("Game 1")
g_root.geometry("600x600+300+50")

Label(g_root, text="WORDLE", font=("Times New Roman", 36)).pack(pady=(20, 10))

# Python variables

user_word = ""
attempts = 0
guessed = False
correct_list = []
button_list = []

# Function

def DisplayLetter(letter_inp):
    global user_word
    global attempts
    row = attempts + 1
    col = len(user_word)
    if letter_inp == "":
        col = len(user_word) + 1
    globals()["letter" + str(row) + "_" + str(col)
              ].config(text=letter_inp)

def ChangeKeyboard(letter, cond, prev_correct):
    colour_list = ["Gray", "Yellow", "Green"]
    globals()["key_" + letter.lower()
              ].config(background=colour_list[max(int(cond), prev_correct * 2)])

def RebindLetters(letter):
    g_root.bind(letter, lambda x: LetterInput(letter.upper()))
    g_root.bind(letter.upper(), lambda x: LetterInput(letter.upper()))

def ResultDisplay(cond, word, i):
    colour_list = ["Gray", "Yellow", "Green"]
    globals()["letter" + str(attempts) + "_" + str(i)
                  ].config(background=colour_list[int(cond[i-1])])
    if i != 5:
        g_root.after(250, lambda: ResultDisplay(cond, word, i+1))
    else:
        for i in button_list:
            globals()[i].config(state=NORMAL)
            # Necessary function since i is a dynamic variable
            RebindLetters(i[-1])

def AttemptResult(cond, word):
    for i in button_list:
        globals()[i].config(state=DISABLED)
        g_root.unbind(i[-1])
        g_root.unbind(i[-1].upper())
    ResultDisplay(cond, word, 1)
    for i in range(len(word)):
        ChangeKeyboard(word[i], cond[i], word[i] in correct_list)

def LetterInput(letter_inp):
    global user_word
    global attempts
    if letter_inp == "ENTER":
        if len(user_word) != 5:
            pass
        elif user_word not in user_word_li and user_word not in word_li:
            error_msg.config(text="Your word is invalid!")
        else:
            error_msg.config(text="")
            cond = ""
            for i in range(5):
                if user_word[i] == target_word[i]:
                    correct_list.append(user_word[i])
                    cond += "2"
                elif user_word[i] in target_word:
                    cond += "1"
                else:
                    cond += "0"
            attempts += 1
            if attempts == 6 and user_word != target_word:
                error_msg.config(text="The word was: " + target_word)
                AttemptResult(cond, user_word)
                g_root.after(1500, lambda: ExitPage(False, attempts))
            elif user_word == target_word:
                error_msg.config(text="The word was: " + target_word)
                AttemptResult("22222", user_word)
                g_root.after(1500, lambda: ExitPage(True, attempts))
            else:
                AttemptResult(cond, user_word)
            user_word = ""
    elif letter_inp == "UNDO":
        if len(user_word) >= 1:
            user_word = user_word[:-1]
            DisplayLetter("")
    else:
        if len(user_word) < 5:
            user_word += letter_inp
            DisplayLetter(letter_inp)

def EditButtonCommands(letter):
    globals()["key_" + letter].config(command=lambda: LetterInput(letter.upper()))
    g_root.bind(letter, lambda x: LetterInput(letter.upper()))
    g_root.bind(letter.upper(), lambda x: LetterInput(letter.upper()))

def LayoutInit():
    global key_ent, key_und
    guess = Frame(g_root)
    guess.pack(pady=10, padx=10)

    w, h = 4, 2

    for i in range(1, 7):
        for j in range(1, 6):
            letter_var = "letter" + str(i) + "_" + str(j)
            globals()[letter_var] = Label(guess, text="", borderwidth=2, 
                                          relief="groove", width=w, height=h)
            globals()[letter_var].grid(row=i-1, column=j-1, padx=w, pady=w)

    keyboardr1 = Frame(g_root)
    keyboardr1.pack(pady=w, padx=10)
    for i in range(len("QWERTYUIOP")):
        key_var = "key_" + "qwertyuiop"[i]
        globals()[key_var] = Button(keyboardr1, text=key_var[-1].upper(), 
                                    width=int(w/2), height=int(h/2))
        EditButtonCommands(key_var[-1])
        globals()[key_var].grid(row=0, column=i+1, padx=w)
        button_list.append(key_var)
    
    keyboardr2 = Frame(g_root)
    keyboardr2.pack(pady=w, padx=10)
    for i in range(len("ASDFGHJKL")):
        key_var = "key_" + "asdfghjkl"[i]
        globals()[key_var] = Button(keyboardr2, text=key_var[-1].upper(), 
                                    width=int(w/2), height=int(h/2))
        EditButtonCommands(key_var[-1])
        globals()[key_var].grid(row=0, column=i+1, padx=w)
        button_list.append(key_var)

    keyboardr3 = Frame(g_root)
    keyboardr3.pack(pady=w, padx=10)
    key_ent = Button(keyboardr3, text="ENTER", width=w+1, height=int(h/2), 
                     command=lambda: LetterInput("ENTER"))
    g_root.bind("<Return>", lambda x: LetterInput("ENTER"))
    key_ent.grid(row=0, column=1, padx=w)

    for i in range(len("zxcvbnm")):
        key_var = "key_" + "zxcvbnm"[i]
        globals()[key_var] = Button(keyboardr3, text=key_var[-1].upper(), 
                                    width=int(w/2), height=int(h/2))
        EditButtonCommands(key_var[-1])
        globals()[key_var].grid(row=0, column=i+2, padx=w)
        button_list.append(key_var)

    key_und = Button(keyboardr3, text="UNDO", width=w+1, height=int(h/2), 
                     command=lambda: LetterInput("UNDO"))
    g_root.bind("<BackSpace>", lambda x: LetterInput("UNDO"))
    key_und.grid(row=0, column=9, padx=w)

    global error_msg
    error_msg = Label(text="")
    error_msg.pack()

def ReturnMenu():
    e_root.destroy()
    subprocess.run(["python", r"Python\11.3\menu\main_menu_tk.py"])

def GoToGame():
    e_root.destroy()
    subprocess.run(["python", r"Python\11.3\game1\game1_main_wordle.py"])

def ExitPage(win, attempts):
    global e_root

    g_root.destroy()

    e_root = Tk(screenName="Game Over")
    e_root.title("Game Over")
    e_root.geometry("600x600+300+50")
    with open(r"Python\11.3\csv_files\user_scores.csv", "r", 
              newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
        prev_high_score = int(rows[-1][1])
        new_high_score = max(int(rows[-1][1]), 7 - attempts)

    win_text = "Congratulations! You guessed the correct word."
    win_score = f"Your score is {7 - attempts}."
    high_score_text = "You also achieved a high score!"
    lose_text = "Game over! You did not get the correct word."
    word_reveal = f"The word was: {target_word.title()}."

    if win:
        Label(e_root, text="YOU WIN", font=("Times New Roman", 36)).pack(pady=20)
        Label(e_root, text=win_text, wraplength=560, justify="left").pack()
        Label(e_root, text=win_score, wraplength=560, justify="left").pack()
        if new_high_score > prev_high_score:
            Label(e_root, text=high_score_text, wraplength=560, 
                  justify="left").pack()
            rows[-1][1] = new_high_score

            with open(r"Python\11.3\csv_files\user_scores.csv", "w", 
                      newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
    else:
        Label(e_root, text="YOU LOSE", font=("Times New Roman", 36)).pack(pady=20)
        Label(e_root, text=lose_text, wraplength=560, justify="left").pack()
    Label(e_root, text=word_reveal, wraplength=560, justify="left").pack()

    scores_list = []
    for i in rows[1:]:
        scores_list.append([i[0], int(i[1])])
    high_score_list = []
    for i in scores_list:
        if len(high_score_list) == 3:
            if i[1] >= high_score_list[0][1]:
                high_score_list.insert(0, i)
                del high_score_list[-1]
            elif i[1] >= high_score_list[1][1]:
                high_score_list.insert(1, i)
                del high_score_list[-1]
            elif i[1] >= high_score_list[2][1]:
                high_score_list.insert(2, i)
                del high_score_list[-1]
        else:
            if len(high_score_list) == 0:
                high_score_list.append(i)
            elif len(high_score_list) == 1:
                if i[1] >= high_score_list[0][1]:
                    high_score_list.insert(0, i)
                else:
                    high_score_list.append(i)
            elif len(high_score_list) == 2:
                if i[1] >= high_score_list[0][1]:
                    high_score_list.insert(0, i)
                elif i[1] >= high_score_list[1][1]:
                    high_score_list.insert(1, i)
                else:
                    high_score_list.append(i)

    Label(e_root, text="LEADERBOARD", font=("Times New Roman", 24)).pack(pady=20)
    leader_frame = Frame(e_root)
    leader_frame.pack()
    
    first_user = Label(leader_frame, text=high_score_list[0][0])
    second_user = Label(leader_frame, text=high_score_list[1][0])
    third_user = Label(leader_frame, text=high_score_list[2][0])
    first_score = Label(leader_frame, text=high_score_list[0][1])
    second_score = Label(leader_frame, text=high_score_list[1][1])
    third_score = Label(leader_frame, text=high_score_list[2][1])

    l_padx = 20
    l_pady = 5
    first_user.grid(row=0, column=0, padx=l_padx, pady=l_pady)
    second_user.grid(row=1, column=0, padx=l_padx, pady=l_pady)
    third_user.grid(row=2, column=0, padx=l_padx, pady=l_pady)
    first_score.grid(row=0, column=1, padx=l_padx, pady=l_pady)
    second_score.grid(row=1, column=1, padx=l_padx, pady=l_pady)
    third_score.grid(row=2, column=1, padx=l_padx, pady=l_pady)

    Label(e_root, text="PLAY AGAIN?", font=("Times New Roman", 24)).pack(pady=20)
    replay_frame = Frame(e_root, width=560)
    replay_frame.pack()
    replay_button = Button(replay_frame, text="Yes (I'm cool)", width=10,
                          command=GoToGame)
    menu_button = Button(replay_frame, text="No (I'm lame)", width=10, 
                          command=ReturnMenu)
    replay_button.grid(row=0, column=0, padx=20)
    menu_button.grid(row=0, column=1, padx=20)

LayoutInit()

g_root.mainloop()
