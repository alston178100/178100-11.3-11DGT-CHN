"""Tkinter code for the main menu"""

from tkinter import *

# Function for when any buttons are pressed
def button_clicked(game_num):
    if name_entry.get() == "":
        error_msg.pack()
    else:
        root.destroy()
        # Accesses a new python file for each game (Avoid lots of lines)
        if game_num == 1:
            with open(r"Python\11.3\game1_wordle_tk.py") as f:
                exec(f.read())
        elif game_num == 2:
            with open(r"Python\11.3\game2\game2_countdown_tk.py") as f:
                exec(f.read())
        elif game_num == 3:
            with open(r"Python\11.3\game3\game3_match_tk.py") as f:
                exec(f.read())
        else:
            with open(
                r"Python\11.3\game4\game4_minesweeper_tk.py") as f:
                exec(f.read())

# Root set up
root = Tk(screenName="Main Menu")
root.geometry("600x600")
root.title("Main Menu")

# Main hading
mm_heading = Label(root, text="Ethan Games Compendium")
mm_heading.pack(pady=20)

# Frame for name entering
name_frame = Frame(root)
Label(name_frame, text="Enter name: ").grid(row=0)
name_entry = Entry(name_frame)
name_entry.grid(row=0, column=1)
name_frame.pack()

# Frames for buttons
game_frame = Frame(root)
button1 = Button(game_frame, text="Wordle", width=25, height=10,
                 command=lambda: button_clicked(1))
button2 = Button(game_frame, text="Countdown", width=25, height=10, 
                 command=lambda: button_clicked(2))
button3 = Button(game_frame, text="Match The Brainrot", width=25, height=10, 
                 command=lambda: button_clicked(3))
button4 = Button(game_frame, text="Minesweeper", width=25, height=10,
                 command=lambda: button_clicked(4))

button1.grid(row=0, pady=25, padx=25)
button2.grid(row=0, column=1)
button3.grid(row=1, pady=25, padx=25)
button4.grid(row=1, column=1)

game_frame.pack()

# Error message if user did not enter username
error_msg = Label(root, text="You did not enter a username!")

root.mainloop()
