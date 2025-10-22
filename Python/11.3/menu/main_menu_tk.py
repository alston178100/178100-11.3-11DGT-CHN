"""Tkinter code for the main menu"""

from tkinter import *
import subprocess
import csv

# Function for when any buttons are pressed

def goto_game(game_num):
    v_root.destroy()
    if game_num == 1:
        subprocess.run(["python", r"Python\11.3\game1\game1_instructions.py"])
    elif game_num == 2:
        subprocess.run(["python", r"Python\11.3\game2\game2_instructions.py"])
    elif game_num == 3:
        subprocess.run(["python", r"Python\11.3\game3\game3_instructions.py"])

def goto_menu():
    v_root.destroy()
    subprocess.run(["python", r"Python\11.3\menu\main_menu_tk.py"])

def button_clicked(game_num):
    global v_root
    username = name_entry.get()
    if username == "":
        error_msg.config(text="You did not enter a username!")
    else:
        root.destroy()
        user_exists = False
        if username in name_li:
            user_exists = True
            text_1 = "Welcome back! Please confirm that this is your "\
            "existing username."
        else:
            with open(r"Python\11.3\csv_files\user_scores.csv", "a", 
                    newline="") as file:
                writer= csv.writer(file)
                writer.writerow([username, 0, 0, 0])
            text_1 = "Welcome! You seem to be a new user. Please confirm " \
            "that this is your new username."
        text_2 = f"Username: {username}"

        v_root = Tk(screenName="Verification")
        v_root.title("Verification")
        v_root.geometry("600x600+300+50")

        Label(v_root, text="WELCOME!!", font=("Times New Roman", 36)).pack(pady=20)
        Label(v_root, text=text_1, wraplength=560,
              justify="left").pack(padx=20, pady=3, anchor="w")
        Label(v_root, text=text_2, wraplength=560, 
              justify="left").pack(padx=40, pady=3, anchor="w")
        if user_exists == True:
            for i in info_li:
                if i["Username"] == username:
                    g1_high = i["Game1_HS"]
                    g2_high = i["Game2_HS"]
                    g3_high = i["Game3_HS"]
                    # Small way of allowing other files to access username
                    info_li.remove(i)
                    info_li.append(i)
                    break
            # Rewrites file so username is now at the end
            with open(r"Python\11.3\csv_files\user_scores.csv", "w", 
                      newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(info_li)

            Label(v_root, text=f"Wordle High Score: {g1_high}", 
                  justify="left").pack(padx=40, pady=3, anchor="w")
            Label(v_root, text=f"Countdown High Score: {g2_high}", 
                  justify="left").pack(padx=40, pady=3, anchor="w")
            Label(v_root, text=f"Minesweeper High Score: {g3_high}",
                  justify="left").pack(padx=40, pady=3, anchor="w")

        confirm_frame = Frame(v_root, width=560)
        confirm_frame.pack()
        confirm_button = Button(confirm_frame, text="Yes, this is me.", width=20,
                            command=lambda: goto_game(game_num))
        deny_button = Button(confirm_frame, text="No, this is not me.", width=20, 
                            command=goto_menu)
        confirm_button.grid(row=0, column=0, padx=20, pady=20)
        deny_button.grid(row=0, column=1, padx=20, pady=20)

# Function for when cursor is hovered over the buttons
def hoverChange(button, hover_colour, exit_colour):
    button.bind("<Enter>", func = lambda x: button.config(
        background=hover_colour))
    button.bind("<Leave>", func = lambda x: button.config(
        background=exit_colour))

# Name list & Variables

name_li = []
info_li = []
fieldnames = ["Username", "Game1_HS", "Game2_HS", "Game3_HS"]
with open(r"Python\11.3\csv_files\user_scores.csv", "r") as file:
    filelines = csv.DictReader(file)
    for i in filelines:
        info_li.append(i)
        name_li.append(i["Username"])

# Root set up
root = Tk(screenName="Main Menu")
root.geometry("600x600+300+50")
root.title("Main Menu")
root.config(cursor="tcross", bg="Floral White")

title_font = "Cambria"
text_font = "Calibri"
text_size = 9

# Main hading
mm_heading = Label(root, text="Ethan Games Compendium", 
                   font=(title_font, 36), bg="Floral White")
mm_heading.pack(pady=20)

# Frame for name entering
name_frame = Frame(root, bg="Floral White")
Label(name_frame, text="Enter name: ", bg="Floral White", 
      font=(text_font, text_size)).grid(row=0)
name_entry = Entry(name_frame, bg="Floral White")
name_entry.grid(row=0, column=1)
name_frame.pack()

# Error message if user did not enter username
error_msg = Label(root, text="", foreground="Red", 
                  font=(text_font, 12, "bold"), bg="Floral White")
error_msg.pack(pady=(15, 0))

# Frames for buttons
game_frame = Frame(root, bg="Floral White")
button1 = Button(game_frame, text="Wordle", width=25, height=10,
                 command=lambda: button_clicked(1), cursor="target", 
                 bg="Powder Blue", activebackground="Powder Blue", 
                 font=(text_font, text_size))
button2 = Button(game_frame, text="Countdown", width=25, height=10, 
                 command=lambda: button_clicked(2), cursor="target", 
                 bg="Powder Blue", activebackground="Powder Blue", 
                 font=(text_font, text_size))
button3 = Button(root, text="Minesweeper", width=25, height=10, 
                 command=lambda: button_clicked(3), cursor="target", 
                 bg="Powder Blue", activebackground="Powder Blue", 
                 font=(text_font, text_size))

button1.grid(row=0, pady=25, padx=25)
button2.grid(row=0, column=1)
game_frame.pack()
button3.pack()

hoverChange(button1, "Medium Turquoise", "Powder Blue")
hoverChange(button2, "Medium Turquoise", "Powder Blue")
hoverChange(button3, "Medium Turquoise", "Powder Blue")

root.mainloop()
