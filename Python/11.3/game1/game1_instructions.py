"""Tkinter code for instructions of game 1: Wordle."""

from tkinter import Tk, Label, Button, Frame
import subprocess


# Functions

def return_menu():
    """Return to menu."""
    g_root.destroy()
    subprocess.run(["python", r"Python\11.3\menu\main_menu_tk.py"])


def go_to_game():
    """Go to main game."""
    g_root.destroy()
    subprocess.run(["python", r"Python\11.3\game1\game1_main_wordle.py"])


# Text

ins_p1 = "Welcome to Wordle! In this game you will have 6 attempts to guess " \
 "a 5 letter word which will not be revealed to you."
ins_p2 = "For each guess, you will be given information on each letter that " \
 "you have typed."
ins_p2_1 = "A green means that your letter is in the word and also in the " \
 "correct position."
ins_p2_2 = "A yellow means that your letter is in the word but not in the " \
 "correct position."
ins_p2_3 = "A gray means that your letter is not in the word."
ins_p3 = "To make a guess, click each button on the bottom keyboard to " \
 "guess a letter for each word and then press the enter button. You can " \
 "also type on your device keyboard."
ins_p4 = "If your word is valid, then we will provide you with the " \
 "information. Otherwise, you will need to enter another valid word."
ins_p5 = "Remember that you only have 6 attempts before you lose, so be " \
 "very wise with your choices. Have fun!!!"
ins_p6 = "NOTE: Any words with repeating letters (E.g. BLEED) will not be " \
 "allowed. This prevents any incorrect information from being provided."
score_p1 = "Your score will be as follows:"
score_p2 = "7 - Number of Tries Remaining."

# Root page

g_root = Tk(screenName="Game 1")
g_root.title("Game 1")
g_root.geometry("600x600+300+50")
g_root.configure(bg="Floral White")

title_font = "Cambria"
text_font = "Calibri"
text_size = 9

Label(g_root, text="WORDLE", font=(title_font, 36), bg="Floral White"
      ).pack(pady=20)

# Creating labels for each text

ins_1 = Label(g_root, text=ins_p1, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
ins_2 = Label(g_root, text=ins_p2, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
ins_2_1 = Label(g_root, text=ins_p2_1, wraplength=560, justify="left",
                font=(text_font, text_size), bg="Floral White")
ins_2_2 = Label(g_root, text=ins_p2_2, wraplength=560, justify="left",
                font=(text_font, text_size), bg="Floral White")
ins_2_3 = Label(g_root, text=ins_p2_3, wraplength=560, justify="left",
                font=(text_font, text_size), bg="Floral White")
ins_3 = Label(g_root, text=ins_p3, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
ins_4 = Label(g_root, text=ins_p4, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
ins_5 = Label(g_root, text=ins_p5, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
# The red foreground makes it easier for the user to see
ins_6 = Label(g_root, text=ins_p6, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White",
              fg="red")

# Some labels are packed so they are slightly indented to the right

ins_1.pack(padx=20, pady=3, anchor="w")
ins_2.pack(padx=20, pady=(3, 1), anchor="w")
ins_2_1.pack(padx=40, pady=1, anchor="w")
ins_2_2.pack(padx=40, pady=1, anchor="w")
ins_2_3.pack(padx=40, pady=(1, 3), anchor="w")
ins_3.pack(padx=20, pady=3, anchor="w")
ins_4.pack(padx=20, pady=3, anchor="w")
ins_5.pack(padx=20, pady=3, anchor="w")
ins_6.pack(padx=20, pady=3, anchor="w")

Label(g_root, text="SCORING", font=(title_font, 24), bg="Floral White"
      ).pack(pady=10)
score_1 = Label(g_root, text=score_p1, wraplength=560, justify="left",
                font=(text_font, text_size), bg="Floral White")
score_2 = Label(g_root, text=score_p2, wraplength=560, justify="left",
                font=(text_font, text_size), bg="Floral White")
score_1.pack(padx=20, pady=3, anchor="w")
score_2.pack(padx=40, pady=3, anchor="w")

# Bottom area

bottom_frame = Frame(g_root, width=560, bg="Floral White")
menu_button = Button(bottom_frame, text="Main Menu", width=10,
                     command=return_menu, font=(text_font, text_size),
                     bg="Floral White")
start_button = Button(bottom_frame, text="Start", width=10,
                      command=go_to_game, font=(text_font, text_size),
                      bg="Floral White")
bottom_frame.pack(side="bottom", pady=20)
menu_button.grid(row=0, column=0, padx=(20, 200))
start_button.grid(row=0, column=1, padx=(200, 20))

g_root.mainloop()
