"""Tkinter code for of game 1: Wordle"""

from tkinter import *
import random
import time

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

# Function

def DisplayLetter(letter_inp):
    global user_word
    global attempts
    row = attempts + 1
    col = len(user_word)
    if row == 1:
        if col == 1:
            letter1_1.config(text=letter_inp)
        if col == 2:
            letter1_2.config(text=letter_inp)
        if col == 3:
            letter1_3.config(text=letter_inp)
        if col == 4:
            letter1_4.config(text=letter_inp)
        if col == 5:
            letter1_5.config(text=letter_inp)
    if row == 2:
        if col == 1:
            letter2_1.config(text=letter_inp)
        if col == 2:
            letter2_2.config(text=letter_inp)
        if col == 3:
            letter2_3.config(text=letter_inp)
        if col == 4:
            letter2_4.config(text=letter_inp)
        if col == 5:
            letter2_5.config(text=letter_inp)
    if row == 3:
        if col == 1:
            letter3_1.config(text=letter_inp)
        if col == 2:
            letter3_2.config(text=letter_inp)
        if col == 3:
            letter3_3.config(text=letter_inp)
        if col == 4:
            letter3_4.config(text=letter_inp)
        if col == 5:
            letter3_5.config(text=letter_inp)
    if row == 4:
        if col == 1:
            letter4_1.config(text=letter_inp)
        if col == 2:
            letter4_2.config(text=letter_inp)
        if col == 3:
            letter4_3.config(text=letter_inp)
        if col == 4:
            letter4_4.config(text=letter_inp)
        if col == 5:
            letter4_5.config(text=letter_inp)
    if row == 5:
        if col == 1:
            letter5_1.config(text=letter_inp)
        if col == 2:
            letter5_2.config(text=letter_inp)
        if col == 3:
            letter5_3.config(text=letter_inp)
        if col == 4:
            letter5_4.config(text=letter_inp)
        if col == 5:
            letter5_5.config(text=letter_inp)
    if row == 6:
        if col == 1:
            letter6_1.config(text=letter_inp)
        if col == 2:
            letter6_2.config(text=letter_inp)
        if col == 3:
            letter6_3.config(text=letter_inp)
        if col == 4:
            letter6_4.config(text=letter_inp)
        if col == 5:
            letter6_5.config(text=letter_inp)

def LetterInput(letter_inp):
    global user_word
    global attempts
    if letter_inp == "ENTER":
        if len(user_word) != 5:
            print("Entered but not enough letters")
        elif user_word not in user_word_li:
            print("Invalid word")
        else:
            attempts += 1
            if attempts == 6:
                time.sleep(1)
                g_root.destroy()
            elif user_word == target_word:
                print(target_word)
                print("Correct word")
                time.sleep(1)
                g_root.destroy()
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
            user_word = ""
    elif letter_inp == "UNDO":
        if len(user_word) >= 1:
            user_word = user_word[:-1]
            print(user_word)
        else:
            print("No letters")
    else:
        if len(user_word) < 5:
            user_word += letter_inp
            DisplayLetter(letter_inp)
        else:
            print("Too many letters")
        print(user_word)

# Some very bad (But necessary) code
def LayoutInit():
    guess = Frame(g_root)
    guess.pack(pady=10, padx=10)

    w, h = 4, 2

    global letter1_1
    global letter1_2
    global letter1_3
    global letter1_4
    global letter1_5
    letter1_1 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter1_2 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter1_3 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter1_4 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter1_5 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    
    global letter2_1
    global letter2_2
    global letter2_3
    global letter2_4
    global letter2_5
    letter2_1 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter2_2 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter2_3 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter2_4 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter2_5 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    
    global letter3_1
    global letter3_2
    global letter3_3
    global letter3_4
    global letter3_5
    letter3_1 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter3_2 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter3_3 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter3_4 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter3_5 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    
    global letter4_1
    global letter4_2
    global letter4_3
    global letter4_4
    global letter4_5
    letter4_1 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter4_2 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter4_3 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter4_4 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter4_5 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    
    global letter5_1
    global letter5_2
    global letter5_3
    global letter5_4
    global letter5_5
    letter5_1 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter5_2 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter5_3 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter5_4 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter5_5 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    
    global letter6_1
    global letter6_2
    global letter6_3
    global letter6_4
    global letter6_5
    letter6_1 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter6_2 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter6_3 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter6_4 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter6_5 = Label(guess, text="", borderwidth=2, relief="groove", 
                    width=w, height=h)
    letter1_1.grid(row=0, column=0, padx=w, pady=w)
    letter1_2.grid(row=0, column=1, padx=w, pady=w)
    letter1_3.grid(row=0, column=2, padx=w, pady=w)
    letter1_4.grid(row=0, column=3, padx=w, pady=w)
    letter1_5.grid(row=0, column=4, padx=w, pady=w)
    letter2_1.grid(row=1, column=0, padx=w, pady=w)
    letter2_2.grid(row=1, column=1, padx=w, pady=w)
    letter2_3.grid(row=1, column=2, padx=w, pady=w)
    letter2_4.grid(row=1, column=3, padx=w, pady=w)
    letter2_5.grid(row=1, column=4, padx=w, pady=w)
    letter3_1.grid(row=2, column=0, padx=w, pady=w)
    letter3_2.grid(row=2, column=1, padx=w, pady=w)
    letter3_3.grid(row=2, column=2, padx=w, pady=w)
    letter3_4.grid(row=2, column=3, padx=w, pady=w)
    letter3_5.grid(row=2, column=4, padx=w, pady=w)
    letter4_1.grid(row=3, column=0, padx=w, pady=w)
    letter4_2.grid(row=3, column=1, padx=w, pady=w)
    letter4_3.grid(row=3, column=2, padx=w, pady=w)
    letter4_4.grid(row=3, column=3, padx=w, pady=w)
    letter4_5.grid(row=3, column=4, padx=w, pady=w)
    letter5_1.grid(row=4, column=0, padx=w, pady=w)
    letter5_2.grid(row=4, column=1, padx=w, pady=w)
    letter5_3.grid(row=4, column=2, padx=w, pady=w)
    letter5_4.grid(row=4, column=3, padx=w, pady=w)
    letter5_5.grid(row=4, column=4, padx=w, pady=w)
    letter6_1.grid(row=5, column=0, padx=w, pady=w)
    letter6_2.grid(row=5, column=1, padx=w, pady=w)
    letter6_3.grid(row=5, column=2, padx=w, pady=w)
    letter6_4.grid(row=5, column=3, padx=w, pady=w)
    letter6_5.grid(row=5, column=4, padx=w, pady=w)

    keyboardr1 = Frame(g_root)
    keyboardr1.pack(pady=w, padx=10)
    key_q = Button(keyboardr1, text="Q", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("Q"))
    key_w = Button(keyboardr1, text="W", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("W"))
    key_e = Button(keyboardr1, text="E", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("E"))
    key_r = Button(keyboardr1, text="R", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("R"))
    key_t = Button(keyboardr1, text="T", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("T"))
    key_y = Button(keyboardr1, text="Y", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("Y"))
    key_u = Button(keyboardr1, text="U", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("U"))
    key_i = Button(keyboardr1, text="I", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("I"))
    key_o = Button(keyboardr1, text="O", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("O"))
    key_p = Button(keyboardr1, text="P", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("P"))
    key_q.grid(row=0, column=1, padx=w)
    key_w.grid(row=0, column=2, padx=w)
    key_e.grid(row=0, column=3, padx=w)
    key_r.grid(row=0, column=4, padx=w)
    key_t.grid(row=0, column=5, padx=w)
    key_y.grid(row=0, column=6, padx=w)
    key_u.grid(row=0, column=7, padx=w)
    key_i.grid(row=0, column=8, padx=w)
    key_o.grid(row=0, column=9, padx=w)
    key_p.grid(row=0, column=10, padx=w)

    keyboardr2 = Frame(g_root)
    keyboardr2.pack(pady=w, padx=10)
    key_a = Button(keyboardr2, text="A", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("A"))
    key_s = Button(keyboardr2, text="S", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("S"))
    key_d = Button(keyboardr2, text="D", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("D"))
    key_f = Button(keyboardr2, text="F", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("F"))
    key_g = Button(keyboardr2, text="G", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("G"))
    key_h = Button(keyboardr2, text="H", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("H"))
    key_j = Button(keyboardr2, text="J", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("J"))
    key_k = Button(keyboardr2, text="K", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("K"))
    key_l = Button(keyboardr2, text="L", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("L"))
    key_a.grid(row=0, column=1, padx=w)
    key_s.grid(row=0, column=2, padx=w)
    key_d.grid(row=0, column=3, padx=w)
    key_f.grid(row=0, column=4, padx=w)
    key_g.grid(row=0, column=5, padx=w)
    key_h.grid(row=0, column=6, padx=w)
    key_j.grid(row=0, column=7, padx=w)
    key_k.grid(row=0, column=8, padx=w)
    key_l.grid(row=0, column=9, padx=w)

    keyboardr3 = Frame(g_root)
    keyboardr3.pack(pady=w, padx=10)
    key_ent = Button(keyboardr3, text="ENTER", width=w+1, height=int(h/2), 
                   command=lambda: LetterInput("ENTER"))
    key_z = Button(keyboardr3, text="Z", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("Z"))
    key_x = Button(keyboardr3, text="X", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("X"))
    key_c = Button(keyboardr3, text="C", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("C"))
    key_v = Button(keyboardr3, text="V", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("V"))
    key_b = Button(keyboardr3, text="B", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("B"))
    key_n = Button(keyboardr3, text="N", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("N"))
    key_m = Button(keyboardr3, text="M", width=int(w/2), height=int(h/2), 
                   command=lambda: LetterInput("M"))
    key_und = Button(keyboardr3, text="UNDO", width=w+1, height=int(h/2), 
                   command=lambda: LetterInput("UNDO"))
    key_ent.grid(row=0, column=1, padx=w)
    key_z.grid(row=0, column=2, padx=w)
    key_x.grid(row=0, column=3, padx=w)
    key_c.grid(row=0, column=4, padx=w)
    key_v.grid(row=0, column=5, padx=w)
    key_b.grid(row=0, column=6, padx=w)
    key_n.grid(row=0, column=7, padx=w)
    key_m.grid(row=0, column=8, padx=w)
    key_und.grid(row=0, column=9, padx=w)

LayoutInit()

g_root.mainloop()
