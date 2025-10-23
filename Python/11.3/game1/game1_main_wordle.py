"""Tkinter code for of game 1: Wordle."""

from tkinter import Tk, Label, Frame, Button, NORMAL, DISABLED
import random
import subprocess
import csv

# Setting up user inputs and target word

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

f = open(r"Python\11.3\txt_files\single_letter_list.txt")
single_word_li = f.readlines()
for i in range(len(single_word_li)):
    single_word_li[i] = single_word_li[i].strip().upper()

g_root = Tk(screenName="Game 1")
g_root.title("Game 1")
g_root.geometry("600x530+300+50")
g_root.configure(bg="Floral White")

Label(g_root, text="WORDLE", font=("Cambria", 36),
      bg="Floral White").pack(pady=(20, 10))


# Function

def display_letter(letter_inp):
    """Display each individual letter."""
    global user_word
    global attempts
    row = attempts + 1
    col = len(user_word)
    if letter_inp == "":
        col = len(user_word) + 1
    globals()["letter" + str(row) + "_" + str(col)
              ].config(text=letter_inp)


def change_keyboard(letter, cond, prev_correct):
    """Change the colour condition on keyboard."""
    colour_list = ["Gray75", "Gold", "Green2"]
    # Some maths used to give the correct colour
    globals()["key_" + letter.lower()
              ].config(
                  background=colour_list[max(int(cond), prev_correct * 2)])


def rebind_letters(letter):
    """Rebind letter after each attempt."""
    g_root.bind(letter, lambda x: letter_input(letter.upper()))
    g_root.bind(letter.upper(), lambda x: letter_input(letter.upper()))


def result_display(cond, word, i):
    """Display the result after each attempmt."""
    colour_list = ["Gray75", "Gold", "Green2"]
    globals()["letter" + str(attempts) + "_" + str(i)
              ].config(background=colour_list[int(cond[i-1])])
    # Sets up the animination for each attempt
    if i != 5:
        g_root.after(250, lambda: result_display(cond, word, i+1))
    else:
        if cond != "22222" and attempts != 6:
            for i in button_list:
                globals()[i].config(state=NORMAL)
                # Necessary function since i is a dynamic variable
                rebind_letters(i[-1])


def attempt_result(cond, word):
    """Keyboard disabling after each attempt."""
    for i in button_list:
        globals()[i].config(state=DISABLED)
        g_root.unbind(i[-1])
        g_root.unbind(i[-1].upper())
    # Disables each button and then displays the result
    result_display(cond, word, 1)
    for i in range(len(word)):
        change_keyboard(word[i], cond[i], word[i] in correct_list)


def letter_input(letter_inp):
    """Input for each letter pressed."""
    global user_word
    global attempts
    if letter_inp == "ENTER":
        # Checks all user inputs if the user pressed enter
        if len(user_word) != 5:
            pass
        elif user_word not in user_word_li and user_word not in word_li:
            error_msg.config(text="Your word is invalid!")
        elif user_word not in single_word_li and user_word in user_word_li:
            error_msg.config(text="Your word has repeated letters!")
        else:
            error_msg.config(text="")
            cond = ""
            for i in range(5):
                if user_word[i] == target_word[i]:
                    correct_list.append(user_word[i])
                    cond += "2"
                elif user_word[i] in target_word:
                    cond += "1"
                else:
                    cond += "0"
            attempts += 1
            if attempts == 6 and user_word != target_word:
                error_msg.config(text="The word was: " + target_word)
                attempt_result(cond, user_word)
                g_root.after(1500, lambda: exit_page(False, attempts))
            elif user_word == target_word:
                error_msg.config(text="The word was: " + target_word)
                attempt_result("22222", user_word)
                g_root.after(1500, lambda: exit_page(True, attempts))
            else:
                attempt_result(cond, user_word)
            user_word = ""
    elif letter_inp == "UNDO":
        # The user has pressed backspace
        if len(user_word) >= 1:
            user_word = user_word[:-1]
            display_letter("")
    else:
        # The user has pressed a letter
        if len(user_word) < 5:
            user_word += letter_inp
            display_letter(letter_inp)


def edit_button_commands(letter):
    """Edit the commands for each variable due to dynamic variables."""
    globals()["key_" + letter].config(command=lambda:
                                      letter_input(letter.upper()))
    g_root.bind(letter, lambda x: letter_input(letter.upper()))
    g_root.bind(letter.upper(), lambda x: letter_input(letter.upper()))


def layout_init():
    """Initialise the layout."""
    global key_ent, key_und
    guess = Frame(g_root, bg="Floral White")
    guess.pack(pady=10, padx=10)

    text_font = "Calibri"
    text_size = 9

    w, h = 4, 2

    # Creates each individual label as a variable using globals
    for i in range(1, 7):
        for j in range(1, 6):
            letter_var = "letter" + str(i) + "_" + str(j)
            globals()[letter_var] = Label(guess, text="", borderwidth=2,
                                          relief="groove", bg="Floral White",
                                          width=w, height=h,
                                          font=(text_font, text_size))
            globals()[letter_var].grid(row=i-1, column=j-1, padx=w, pady=w)

    # Row 1 display
    keyboardr1 = Frame(g_root, bg="Floral White")
    keyboardr1.pack(pady=w, padx=10)
    for i in range(len("QWERTYUIOP")):
        key_var = "key_" + "qwertyuiop"[i]
        globals()[key_var] = Button(keyboardr1, text=key_var[-1].upper(),
                                    width=int(w/2), height=int(h/2),
                                    font=(text_font, text_size))
        edit_button_commands(key_var[-1])
        globals()[key_var].grid(row=0, column=i+1, padx=w)
        button_list.append(key_var)

    # Row 2 display
    keyboardr2 = Frame(g_root, bg="Floral White")
    keyboardr2.pack(pady=w, padx=10)
    for i in range(len("ASDFGHJKL")):
        key_var = "key_" + "asdfghjkl"[i]
        globals()[key_var] = Button(keyboardr2, text=key_var[-1].upper(),
                                    width=int(w/2), height=int(h/2),
                                    font=(text_font, text_size))
        edit_button_commands(key_var[-1])
        globals()[key_var].grid(row=0, column=i+1, padx=w)
        button_list.append(key_var)

    # Row 3 display
    keyboardr3 = Frame(g_root, bg="Floral White")
    keyboardr3.pack(pady=w, padx=10)
    key_ent = Button(keyboardr3, text="ENTER", width=w+1, height=int(h/2),
                     command=lambda: letter_input("ENTER"),
                     font=(text_font, text_size))
    g_root.bind("<Return>", lambda x: letter_input("ENTER"))
    key_ent.grid(row=0, column=1, padx=w)

    for i in range(len("zxcvbnm")):
        key_var = "key_" + "zxcvbnm"[i]
        globals()[key_var] = Button(keyboardr3, text=key_var[-1].upper(),
                                    width=int(w/2), height=int(h/2),
                                    font=(text_font, text_size))
        edit_button_commands(key_var[-1])
        globals()[key_var].grid(row=0, column=i+2, padx=w)
        button_list.append(key_var)

    key_und = Button(keyboardr3, text="UNDO", width=w+1, height=int(h/2),
                     command=lambda: letter_input("UNDO"),
                     font=(text_font, text_size))
    g_root.bind("<BackSpace>", lambda x: letter_input("UNDO"))
    key_und.grid(row=0, column=9, padx=w)

    global error_msg
    error_msg = Label(text="", bg="Floral White", font=(text_font, text_size))
    error_msg.pack()


def return_menu():
    """Return to the menu."""
    e_root.destroy()
    subprocess.run(["python", r"Python\11.3\menu\main_menu_tk.py"])


def go_to_game():
    """Replay the game."""
    e_root.destroy()
    subprocess.run(["python", r"Python\11.3\game1\game1_main_wordle.py"])


def exit_page(win, attempts):
    """Run after the game is ended."""
    global e_root

    g_root.destroy()

    e_root = Tk(screenName="Game Over")
    e_root.title("Game Over")
    e_root.geometry("600x500+300+50")
    e_root.configure(bg="Floral White")

    title_font = "Cambria"
    text_font = "Calibri"
    text_size = 9

    # Reads the csv file for user score
    with open(r"Python\11.3\csv_files\user_scores.csv", "r",
              newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
        prev_high_score = int(rows[-1][1])
        new_high_score = max(int(rows[-1][1]), 7 - attempts)

    win_text = "Congratulations! You guessed the correct word."
    win_score = f"Your score is {7 - attempts}."
    high_score_text = "You also achieved a high score!"
    lose_text = "Game over! You did not get the correct word."
    word_reveal = f"The word was: {target_word.title()}."

    # Outputs different texts depending on win or lose
    if win:
        Label(e_root, text="YOU WIN", font=(title_font, 36),
              bg="Floral White").pack(pady=20)
        Label(e_root, text=win_text, wraplength=560, justify="left",
              bg="Floral White", font=(text_font, text_size)).pack()
        Label(e_root, text=win_score, wraplength=560, justify="left",
              bg="Floral White", font=(text_font, text_size)).pack()
        if new_high_score > prev_high_score:
            Label(e_root, text=high_score_text, wraplength=560,
                  justify="left", bg="Floral White",
                  font=(text_font, text_size)).pack()
            rows[-1][1] = new_high_score

            with open(r"Python\11.3\csv_files\user_scores.csv", "w",
                      newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
    else:
        Label(e_root, text="YOU LOSE", font=("Times New Roman", 36),
              bg="Floral White").pack(pady=20)
        Label(e_root, text=lose_text, wraplength=560, justify="left",
              bg="Floral White", font=(text_font, text_size)).pack()
    Label(e_root, text=word_reveal, wraplength=560, justify="left",
          bg="Floral White", font=(text_font, text_size)).pack()

    # Checks for any leaderboard changes
    scores_list = []
    for i in rows[1:]:
        scores_list.append([i[0], int(i[1])])
    high_score_list = [["-", 0], ["-", 0], ["-", 0]]
    for i in scores_list:
        if len(high_score_list) == 3:
            if i[1] >= high_score_list[0][1]:
                high_score_list.insert(0, i)
                del high_score_list[-1]
            elif i[1] >= high_score_list[1][1]:
                high_score_list.insert(1, i)
                del high_score_list[-1]
            elif i[1] >= high_score_list[2][1]:
                high_score_list.insert(2, i)
                del high_score_list[-1]
        else:
            if len(high_score_list) == 0:
                high_score_list.append(i)
            elif len(high_score_list) == 1:
                if i[1] >= high_score_list[0][1]:
                    high_score_list.insert(0, i)
                else:
                    high_score_list.append(i)
            elif len(high_score_list) == 2:
                if i[1] >= high_score_list[0][1]:
                    high_score_list.insert(0, i)
                elif i[1] >= high_score_list[1][1]:
                    high_score_list.insert(1, i)
                else:
                    high_score_list.append(i)

    Label(e_root, text="LEADERBOARD", font=(title_font, 24),
          bg="Floral White").pack(pady=20)
    leader_frame = Frame(e_root, bg="Floral White")
    leader_frame.pack()

    # Used if there are not enough non-zero score inputs
    for i in high_score_list:
        if i[1] == 0:
            i[0] = "-"
            i[1] = "-"

    # High scores stored in a grid
    first_user = Label(leader_frame, text=high_score_list[0][0],
                       bg="Floral White", font=(text_font, text_size))
    second_user = Label(leader_frame, text=high_score_list[1][0],
                        bg="Floral White", font=(text_font, text_size))
    third_user = Label(leader_frame, text=high_score_list[2][0],
                       bg="Floral White", font=(text_font, text_size))
    first_score = Label(leader_frame, text=high_score_list[0][1],
                        bg="Floral White", font=(text_font, text_size))
    second_score = Label(leader_frame, text=high_score_list[1][1],
                         bg="Floral White", font=(text_font, text_size))
    third_score = Label(leader_frame, text=high_score_list[2][1],
                        bg="Floral White", font=(text_font, text_size))

    l_padx = 20
    l_pady = 5
    first_user.grid(row=0, column=0, padx=l_padx, pady=l_pady)
    second_user.grid(row=1, column=0, padx=l_padx, pady=l_pady)
    third_user.grid(row=2, column=0, padx=l_padx, pady=l_pady)
    first_score.grid(row=0, column=1, padx=l_padx, pady=l_pady)
    second_score.grid(row=1, column=1, padx=l_padx, pady=l_pady)
    third_score.grid(row=2, column=1, padx=l_padx, pady=l_pady)

    # Asks user to play again or return to menu
    Label(e_root, text="PLAY AGAIN?", font=(title_font, 24),
          bg="Floral White").pack(pady=20)
    replay_frame = Frame(e_root, width=560, bg="Floral White")
    replay_frame.pack()
    replay_button = Button(replay_frame, text="Yes", width=10,
                           command=go_to_game,
                           bg="Floral White", font=(text_font, text_size))
    menu_button = Button(replay_frame, text="No", width=10,
                         command=return_menu,
                         bg="Floral White", font=(text_font, text_size))
    replay_button.grid(row=0, column=0, padx=20)
    menu_button.grid(row=0, column=1, padx=20)


# Python variables

user_word = ""
attempts = 0
guessed = False
correct_list = []
button_list = []

layout_init()

g_root.mainloop()
