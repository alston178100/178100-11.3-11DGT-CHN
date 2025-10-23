"""Tkinter code for the main menu."""

from tkinter import Label, Frame, Button, Tk, Entry
import subprocess
import csv


# Functions for when any buttons are pressed

def goto_game(game_num, user_exists, username):
    """Go to the desired game."""
    if not user_exists:
        with open(r"Python\11.3\csv_files\user_scores.csv", "a",
                  newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, 0, 0, 0])
    v_root.destroy()
    # Sends user to specific game instructions page
    if game_num == 1:
        subprocess.run(["python", r"Python\11.3\game1\game1_instructions.py"])
    elif game_num == 2:
        subprocess.run(["python", r"Python\11.3\game2\game2_instructions.py"])
    elif game_num == 3:
        subprocess.run(["python", r"Python\11.3\game3\game3_instructions.py"])


def goto_menu():
    """Return to menu."""
    v_root.destroy()
    subprocess.run(["python", r"Python\11.3\menu\main_menu_tk.py"])


def button_clicked(game_num):
    """Run when a game button is clicked."""
    global v_root
    username = name_entry.get().rstrip()
    # Checks username limitations
    if username == "":
        error_msg.config(text="You did not enter a username!")
    elif len(username) > 20:
        error_msg.config(text="Your username has to be 20 letters or less.")
    elif not username.isalnum():
        error_msg.config(text="Your username can only have "
                         "letters and/or numbers (No spaces).")
    else:
        root.destroy()
        user_exists = False
        # Checks whether the username exists
        if username in name_li:
            user_exists = True
            text_1 = "Welcome back! Please confirm that this is your "\
                "existing username."
        else:
            text_1 = "Welcome! You seem to be a new user. Please confirm " \
                f"that your username is {username}."
            games = ["Wordle", "Countdown", "Minesweeper"]
            text_2 = f"Your selected game is {games[game_num-1]}."

        # Creates a new root for verification
        v_root = Tk(screenName="Verification")
        v_root.title("Verification")
        v_root.geometry("450x330+300+50")
        v_root.config(cursor="tcross", bg="Floral White")
        v_frame = Frame(v_root, bg="Floral White")

        title_font = "Cambria"
        text_font = "Calibri"
        text_size = 9

        Label(v_root, text="Welcome!", font=(title_font, 36),
              bg="Floral White").pack(pady=20)
        Label(v_root, text=text_1, wraplength=410, bg="Floral White",
              justify="left", font=(text_font, text_size)).pack(
                  padx=20, pady=3, anchor="w")

        if user_exists is True:
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

            # Shows usernames in grid form
            v_frame.pack()
            Label(v_frame, text="Username", wraplength=340, bg="Floral White",
                  justify="left", font=(text_font, text_size)
                  ).grid(row=0, column=0, padx=20, pady=5)
            Label(v_frame, text=username, wraplength=340, bg="Floral White",
                  justify="left", font=(text_font, text_size)
                  ).grid(row=0, column=1, padx=20, pady=5)
            Label(v_frame, text="Wordle High Score", wraplength=340,
                  bg="Floral White",
                  justify="left", font=(text_font, text_size)
                  ).grid(row=1, column=0, padx=20, pady=5)
            Label(v_frame, text=g1_high, wraplength=340, bg="Floral White",
                  justify="left", font=(text_font, text_size)
                  ).grid(row=1, column=1, padx=20, pady=5)
            Label(v_frame, text="Countdown High Score", wraplength=340,
                  bg="Floral White", justify="left",
                  font=(text_font, text_size)
                  ).grid(row=2, column=0, padx=20, pady=5)
            Label(v_frame, text=g2_high, wraplength=340, bg="Floral White",
                  justify="left", font=(text_font, text_size)
                  ).grid(row=2, column=1, padx=20, pady=5)
            Label(v_frame, text="Minesweeper High Score", wraplength=340,
                  bg="Floral White", justify="left",
                  font=(text_font, text_size)
                  ).grid(row=3, column=0, padx=20, pady=5)
            Label(v_frame, text=g3_high, wraplength=340, bg="Floral White",
                  justify="left", font=(text_font, text_size)
                  ).grid(row=3, column=1, padx=20, pady=5)
        else:
            Label(v_root, text=text_2, wraplength=410, bg="Floral White",
                  justify="left", font=(text_font, text_size)).pack(
                  padx=20, pady=3, anchor="w")

        # Frame for confirming username
        confirm_frame = Frame(v_root, width=560, bg="Floral White")
        confirm_frame.pack()
        confirm_button = Button(confirm_frame, text="Yes, this is me",
                                width=20,
                                command=lambda: goto_game(
                                 game_num, user_exists, username),
                                cursor="target", bg="LightBlue1",
                                activebackground="LightBlue1",
                                font=(text_font, text_size))
        deny_button = Button(confirm_frame, text="No, this is not me",
                             width=20,
                             command=goto_menu, cursor="target",
                             bg="LightBlue1", activebackground="LightBlue1",
                             font=(text_font, text_size))
        confirm_button.grid(row=0, column=0, padx=20, pady=20)
        deny_button.grid(row=0, column=1, padx=20, pady=20)

        hover_change(confirm_button, "SkyBlue1", "LightBlue1")
        hover_change(deny_button, "SkyBlue1", "LightBlue1")


def quit_game():
    """Quit the window."""
    root.quit()


# Function for when cursor is hovered over the buttons
def hover_change(button, hover_colour, exit_colour):
    """Run when a user hovers over a button."""
    button.bind("<Enter>", func=lambda x: button.config(
        background=hover_colour))
    button.bind("<Leave>", func=lambda x: button.config(
        background=exit_colour))


# Name list & Variables

name_li = []
info_li = []
# Fieldnames are used for the csv file
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
mm_heading = Label(root, text="Alston Games Compendium",
                   font=(title_font, 36), bg="Floral White")
mm_heading.pack(pady=20)

# Frame for name entering
name_frame = Frame(root, bg="Floral White")
Label(name_frame, text="Enter Username: ", bg="Floral White",
      font=(text_font, text_size)).grid(row=0)
name_entry = Entry(name_frame)
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
                 bg="LightBlue1", activebackground="LightBlue1",
                 font=(text_font, text_size))
button2 = Button(game_frame, text="Countdown", width=25, height=10,
                 command=lambda: button_clicked(2), cursor="target",
                 bg="LightBlue1", activebackground="LightBlue1",
                 font=(text_font, text_size))
button3 = Button(root, text="Minesweeper", width=25, height=10,
                 command=lambda: button_clicked(3), cursor="target",
                 bg="LightBlue1", activebackground="LightBlue1",
                 font=(text_font, text_size))
button4 = Button(root, text="Quit", width=10, height=1,
                 command=lambda: quit_game(), cursor="target",
                 bg="LightBlue1", activebackground="LightBlue1",
                 font=(text_font, text_size))

button1.grid(row=0, pady=25, padx=25)
button2.grid(row=0, column=1)
game_frame.pack()
button3.pack()
button4.place(rely=1, relx=0, anchor="sw", x=10, y=-10)

# Connects to the change when a button is hovered over

hover_change(button1, "SkyBlue1", "LightBlue1")
hover_change(button2, "SkyBlue1", "LightBlue1")
hover_change(button3, "SkyBlue1", "LightBlue1")
hover_change(button4, "SkyBlue1", "LightBlue1")

root.mainloop()
