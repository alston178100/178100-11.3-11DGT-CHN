"""Tkinter code for instructions of game 2: Countdown"""

from tkinter import *
import subprocess

# Functions

def ReturnMenu():
    g_root.destroy()
    subprocess.run(["python", r"Python\11.3\menu\main_menu_tk.py"])

def GoToGame():
    g_root.destroy()
    subprocess.run(["python", r"Python\11.3\game3\game3_minesweeper_tk.py"])

# Text

ins_p1 = "Welcome to Minesweeper! This is a game where you have to clear a " \
"16 x 16 square without accidentally clicking on a mine."
ins_p2 = "To start, click on a square. There will be a yellow highlighted " \
"square which guarantees that there is no mine for you to start."
ins_p3 = "Each number represents the number of mines adjacent to that " \
"square. This includes to the diagonals, meaning there can be up to 8 " \
"adjacent squares."
ins_p4 = "You can right click with a mouse on a non-revealed square to " \
"place a flag. You can right click that square again to remove the flag. " \
"Flagging is used for you to keep track of the mines, but is not required."
ins_p5 = "Clicking on a mine will result in the game being over, and you " \
"must click on every non-mine square to win the game."
ins_p6 = "You can also middle click to implement chording, which is a " \
"strategy commonly used by more experienced minesweeper players."
ins_p7 = "Remember that there is a timer as well, and your points will " \
"decrease as you take longer. Have fun!!"
ins_p8 = "WARNING: Users may experience slight lag when first trying to " \
"use the flagging function."

score_p1 = "Your score will be as follows:" 
score_p2 = "300 - time taken in seconds"

# Root page

g_root = Tk(screenName="Game 3")
g_root.title("Game 3")
g_root.geometry("600x600+300+50")
g_root.configure(bg="Floral White")

title_font = "Cambria"
text_font = "Calibri"
text_size = 9

Label(g_root, text="MINESWEEPER", font=(title_font, 36), bg="Floral White"
      ).pack(pady=20)

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
ins_8 = Label(g_root, text=ins_p8, wraplength=560, justify="left", fg="red",
              font=(text_font, text_size), bg="Floral White")

ins_1.pack(padx=20, pady=3, anchor="w")
ins_2.pack(padx=20, pady=3, anchor="w")
ins_3.pack(padx=20, pady=3, anchor="w")
ins_4.pack(padx=20, pady=3, anchor="w")
ins_5.pack(padx=20, pady=3, anchor="w")
ins_6.pack(padx=20, pady=3, anchor="w")
ins_7.pack(padx=20, pady=3, anchor="w")
ins_8.pack(padx=20, pady=3, anchor="w")

Label(g_root, text="SCORING", font=(title_font, 24), bg="Floral White"
      ).pack(pady=10)
score_1 = Label(g_root, text=score_p1, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
score_2 = Label(g_root, text=score_p2, wraplength=560, justify="left",
              font=(text_font, text_size), bg="Floral White")
score_1.pack(padx=20, pady=3, anchor="w")
score_2.pack(padx=40, pady=3, anchor="w")

bottom_frame = Frame(g_root, width=560, bg="Floral White")
menu_button = Button(bottom_frame, text="Main Menu", width=10, 
                     command=ReturnMenu, font=(text_font, text_size), 
                     bg="Floral White")
start_button = Button(bottom_frame, text="Start", width=10, 
                      command=GoToGame, font=(text_font, text_size), 
                      bg="Floral White")
bottom_frame.pack(side="bottom", pady=20)
menu_button.grid(row=0,column=0, padx=(20, 200))
start_button.grid(row=0, column=1, padx=(200, 20))

g_root.mainloop()
