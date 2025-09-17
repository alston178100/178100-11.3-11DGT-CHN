"""Tkinter code for the main menu"""

from tkinter import *
import subprocess
import csv

# Function for when any buttons are pressed
def button_clicked(game_num):
    username = name_entry.get()
    if username == "":
        error_msg.config(text="You did not enter a username!")
    else:
        root.destroy()
        if username in name_li:
            print("Username already exists")
        else:
            with open(r"Python\11.3\csv_files\user_scores.csv", "a", 
                    newline="") as file:
                writer= csv.writer(file)
                writer.writerow([username, 0, 0, 0, 0])
        # Accesses a new python file for each game (Avoid lots of lines)
        if game_num == 1:
            subprocess.run(["python", 
                            r"Python\11.3\game1\game1_instructions.py"])
        elif game_num == 2:
            subprocess.run(["python", 
                            r"Python\11.3\game2\game2_instructions.py"])
        elif game_num == 3:
            subprocess.run(["python", 
                            r"Python\11.3\game3\game3_instructions.py"])
        else:
            subprocess.run(["python", 
                            r"Python\11.3\game4\game4_instructions.py"])

def hoverChange(button, hover_colour, exit_colour):
    button.bind("<Enter>", func = lambda x: button.config(
        background=hover_colour))
    button.bind("<Leave>", func = lambda x: button.config(
        background=exit_colour))

# Name list

name_li = []
with open(r"Python\11.3\csv_files\user_scores.csv", "r") as file:
    filelines = csv.DictReader(file)
    for i in filelines:
        name_li.append(i["Username"])

# Root set up
root = Tk(screenName="Main Menu")
root.geometry("600x600+300+50")
root.title("Main Menu")
root.config(cursor="tcross")

# Main hading
mm_heading = Label(root, text="Ethan Games Compendium", 
                   font=("Times New Roman", 36))
mm_heading.pack(pady=20)

# Frame for name entering
name_frame = Frame(root)
Label(name_frame, text="Enter name: ").grid(row=0)
name_entry = Entry(name_frame)
name_entry.grid(row=0, column=1)
name_frame.pack()

# Error message if user did not enter username
error_msg = Label(root, text="", foreground="Red", 
                  font=("Arial", 11, "bold"))
error_msg.pack(pady=(15, 0))

# Frames for buttons
game_frame = Frame(root)
button1 = Button(game_frame, text="Wordle", width=25, height=10,
                 command=lambda: button_clicked(1), cursor="target", 
                 bg="Powder Blue", activebackground="Powder Blue")
button2 = Button(game_frame, text="Countdown", width=25, height=10, 
                 command=lambda: button_clicked(2), cursor="target", 
                 bg="Powder Blue", activebackground="Powder Blue")
button3 = Button(game_frame, text="Match The Brainrot", width=25, height=10, 
                 command=lambda: button_clicked(3), cursor="target", 
                 bg="Powder Blue", activebackground="Powder Blue")
button4 = Button(game_frame, text="Minesweeper", width=25, height=10,
                 command=lambda: button_clicked(4), cursor="target", 
                 bg="Powder Blue", activebackground="Powder Blue")

button1.grid(row=0, pady=25, padx=25)
button2.grid(row=0, column=1)
button3.grid(row=1, pady=25, padx=25)
button4.grid(row=1, column=1)

hoverChange(button1, "Medium Turquoise", "Powder Blue")
hoverChange(button2, "Medium Turquoise", "Powder Blue")
hoverChange(button3, "Medium Turquoise", "Powder Blue")
hoverChange(button4, "Medium Turquoise", "Powder Blue")

game_frame.pack()

root.mainloop()
