"""Tkinter code for instructions of game 2: Countdown"""

from tkinter import *
import subprocess

# Functions

def ReturnMenu():
    g_root.destroy()
    subprocess.run(["python", r"Python\11.3\menu\main_menu_tk.py"])

def GoToGame():
    g_root.destroy()
    subprocess.run(["python", r"Python\11.3\game2\game2_main_countdown.py"])

# Text

ins_p1 = "Welcome to Countdown! This is a math-based game, where you try to " \
"get as close to the target number as possible." 
ins_p2 = "For each guess, you will be given information on each letter that " \
"you have guessed."
ins_p2_1 = "A green means that your letter is in the word and also in the " \
"correct position."
ins_p2_2 = "A yellow means that your letter is in the word, but not in the " \
"correct position."
ins_p2_3 = "A gray means that your letter is not in the word."
ins_p3 = "To make a guess, click each button on the bottom keyboard to guess " \
"a letter for each word and then press the enter button."
ins_p4 = "If your word is valid, then we will provide you with the " \
"information. Otherwise, you will need to enter another valid word."
ins_p5 = "Remember that you only have 6 attempts before you lose, so be very " \
"wise with your choices. Have fun!!!"
score_p1 = "Your score will be 7 - number of tries remaining."

# Root page

g_root = Tk(screenName="Game 1")
g_root.title("Game 1")
g_root.geometry("600x600+300+50")

Label(g_root, text="GAME 1", font=("Times New Roman", 36)).pack(pady=20)

ins_1 = Label(g_root, text=ins_p1, wraplength=560, justify="left")
ins_2 = Label(g_root, text=ins_p2, wraplength=560, justify="left")
ins_2_1 = Label(g_root, text=ins_p2_1, wraplength=560, justify="left")
ins_2_2 = Label(g_root, text=ins_p2_2, wraplength=560, justify="left")
ins_2_3 = Label(g_root, text=ins_p2_3, wraplength=560, justify="left")
ins_3 = Label(g_root, text=ins_p3, wraplength=560, justify="left")
ins_4 = Label(g_root, text=ins_p4, wraplength=560, justify="left")
ins_5 = Label(g_root, text=ins_p5, wraplength=560, justify="left")
ins_1.pack(padx=20, pady=3, anchor="w")
ins_2.pack(padx=20, pady=(3, 1), anchor="w")
ins_2_1.pack(padx=40, pady=1, anchor="w")
ins_2_2.pack(padx=40, pady=1, anchor="w")
ins_2_3.pack(padx=40, pady=(1, 3), anchor="w")
ins_3.pack(padx=20, pady=3, anchor="w")
ins_4.pack(padx=20, pady=3, anchor="w")
ins_5.pack(padx=20, pady=3, anchor="w")

Label(g_root, text="SCORING", font=("Times New Roman", 24)).pack(pady=10)
score_1 = Label(g_root, text=score_p1, wraplength=560, justify="left")
score_1.pack(padx=20, pady=3, anchor="w")

bottom_frame = Frame(g_root, width=560)
menu_button = Button(bottom_frame, text="Main Menu", width=10, 
                     command=ReturnMenu)
start_button = Button(bottom_frame, text="Start", width=10, 
                      command=GoToGame)
bottom_frame.pack(side="bottom", pady=20)
menu_button.grid(row=0,column=0, padx=(20, 200))
start_button.grid(row=0, column=1, padx=(200, 20))

g_root.mainloop()
