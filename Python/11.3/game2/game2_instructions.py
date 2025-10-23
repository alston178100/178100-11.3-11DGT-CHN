"""Tkinter code for instructions of game 2: Countdown."""

from tkinter import Tk, Label, Frame, Button
import subprocess


# Functions

def return_menu():
    """Return to menu."""
    g_root.destroy()
    subprocess.run(["python", r"Python\11.3\menu\main_menu_tk.py"])


def go_to_game():
    """Go to main game."""
    g_root.destroy()
    subprocess.run(["python", r"Python\11.3\game2\game2_main_countdown.py"])


# Text

ins_p1 = "Welcome to Countdown! This is a math-based game, where you try to " \
 "get as close to the target number as possible in 60 seconds using the " \
 "6 numbers that you have."
ins_p2 = "For each attempt, press on two numbers and a math operator."
ins_p3 = "Then, press enter to submit your step, which removes the two " \
 "numbers you selected and inserts a number made by these two numbers and " \
 "the operator."
ins_p4 = "Division will only work if they divide to an integer (i.e. " \
 "Dividing to a decimal is NOT allowed). Subtraction to a zero will " \
 "also NOT be allowed."
ins_p5 = "Continue this process until you get to one number, which you " \
 "should make as close to the target number as possible."
ins_p6 = "You will get some amount of points if your number is within 50 of " \
 "the target number, and the amount decreases as you are further away."
ins_p7 = "There will also be a timer from 60 seconds, and not submitting a " \
 "number before the time is up will result in no points."
ins_p8 = "You are also able to undo your move, and this will go back to " \
 "your previous group of numbers."
ins_p9 = "Have fun!!"

score_p1 = "Your score will be as follows:"
score_p2 = "Time Left × (50 - Absolute Difference Between Target Number and " \
 "User Number)"

# Root page

g_root = Tk(screenName="Game 2")
g_root.title("Game 2")
g_root.geometry("600x600+300+50")
g_root.configure(bg="Floral White")

# Fonts for the title and texts

title_font = "Cambria"
text_font = "Calibri"
text_size = 9

Label(g_root, text="COUNTDOWN", font=(title_font, 36), bg="Floral White"
      ).pack(pady=20)

# Label set up for the instruction text

ins_1 = Label(g_root, text=ins_p1, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
ins_2 = Label(g_root, text=ins_p2, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
ins_3 = Label(g_root, text=ins_p3, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
ins_4 = Label(g_root, text=ins_p4, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
ins_5 = Label(g_root, text=ins_p5, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
ins_6 = Label(g_root, text=ins_p6, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
ins_7 = Label(g_root, text=ins_p7, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
ins_8 = Label(g_root, text=ins_p8, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
ins_9 = Label(g_root, text=ins_p9, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")

ins_1.pack(padx=20, pady=3, anchor="w")
ins_2.pack(padx=20, pady=3, anchor="w")
ins_3.pack(padx=20, pady=3, anchor="w")
ins_4.pack(padx=20, pady=3, anchor="w")
ins_5.pack(padx=20, pady=3, anchor="w")
ins_6.pack(padx=20, pady=3, anchor="w")
ins_7.pack(padx=20, pady=3, anchor="w")
ins_8.pack(padx=20, pady=3, anchor="w")
ins_9.pack(padx=20, pady=3, anchor="w")

# Scoring system given to user

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
