"""Tkinter code for of game 1: Wordle"""

from tkinter import *

g_root = Tk(screenName="Game 1")
g_root.title("Game 1")
g_root.geometry("600x600+300+50")

Label(g_root, text="WORDLE", font=("Times New Roman", 36)).pack(pady=20)

guess = Frame(g_root)
guess.pack(pady=10, padx=10)

# Some very bad (But necessary) code
def layout_init():
    w, h = 4, 2
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

    

layout_init()

g_root.mainloop()
