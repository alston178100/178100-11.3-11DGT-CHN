"""Tkinter code for game 2: Countdown."""

from tkinter import Tk, Button, Frame, Label
import random
import subprocess
import csv

g_root = Tk(screenName="Game 2")
g_root.title("Game 2")
g_root.geometry("600x600+300+50")
g_root.configure(bg="Floral White")


# Functions

def get_numbers():
    """Find the target number."""
    global target_num
    large_ints = [25, 50, 75, 100]
    num_set = set()

    for i in range(random.randint(1, 4)):
        num_set.add(large_ints[random.randint(0, 3)])

    while len(num_set) < 6:
        num_set.add(random.randint(1, 10))

    # Initialing target number

    while True:
        attempt_target = list(num_set)

        for i in range(5, 0, -1):
            operator = random.randint(1, 4)

            rand_1 = random.randint(0, i)
            num_1 = attempt_target[rand_1]
            del attempt_target[rand_1]

            rand_2 = random.randint(0, i-1)
            num_2 = attempt_target[rand_2]
            del attempt_target[rand_2]

            if operator == 4:
                if (num_1 / num_2).is_integer():
                    attempt_target.append(int(num_1 / num_2))
                elif (num_2 / num_1).is_integer():
                    attempt_target.append(int(num_2 / num_1))
                else:
                    operator = random.randint(1, 3)
            if operator == 3:
                attempt_target.append(num_1 * num_2)
            elif operator == 2:
                attempt_target.append(abs(num_1 - num_2))
            elif operator == 1:
                attempt_target.append(num_1 + num_2)

        # The target number must be at most 999
        if attempt_target[0] <= 999 and attempt_target[0] > 0:
            target_num = attempt_target[0]
            break

    num_set = list(num_set)
    num_set.append(target_num)
    return num_set


def modify_buttons_remove():
    """Remove the button after each attempt."""
    global temp_label_1
    global temp_label_2
    button_count = len(user_nums)
    # The display depends on number of buttons left
    if button_count == 5:
        num_5.grid_forget()
        num_0.config(text=user_nums[0])
        num_1.config(text=user_nums[1])
        num_2.config(text=user_nums[2])
        num_3.config(text=user_nums[3])
        num_4.config(text=user_nums[4])
    elif button_count == 4:
        num_4.grid_forget()
        num_0.config(text=user_nums[0])
        num_1.config(text=user_nums[1])
        num_2.config(text=user_nums[2])
        num_3.config(text=user_nums[3])
    elif button_count == 3:
        num_3.grid_forget()
        num_0.config(text=user_nums[0])
        num_1.config(text=user_nums[1])
        num_2.config(text=user_nums[2])
    elif button_count == 2:
        num_2.grid_forget()
        num_0.config(text=user_nums[0])
        num_1.config(text=user_nums[1])
        # Temporary labels ensure that the final numbers are centered
        temp_label_1 = Label(clickables, width=b_width, height=b_height,
                             bg="Floral White")
        # Hard coded value b_pad + 5 due to strange width differences
        temp_label_1.grid(row=0, column=2, padx=b_pad+10, pady=b_pad)
    elif button_count == 1:
        num_1.grid_forget()
        num_0.config(text=user_nums[0])
        num_0.grid(row=0, column=1, padx=b_pad, pady=b_pad)
        temp_label_2 = Label(clickables, width=b_width, height=b_height,
                             bg="Floral White")
        temp_label_2.grid(row=0, column=0, padx=b_pad+10, pady=b_pad)
        finish_button.pack()


def modify_buttons_add():
    """Add one button after each undo."""
    button_count = len(user_nums)
    # This display depends on the number of buttons left
    if button_count == 2:
        num_0.config(text=user_nums[0])
        num_1.config(text=user_nums[1])
        # The temporary labels are removed so they don't take up space
        temp_label_2.grid_forget()
        num_0.grid(row=0, column=0, padx=b_pad, pady=b_pad)
        num_1.grid(row=0, column=1, padx=b_pad, pady=b_pad)
        finish_button.pack_forget()
    elif button_count == 3:
        num_0.config(text=user_nums[0])
        num_1.config(text=user_nums[1])
        num_2.config(text=user_nums[2])
        temp_label_1.grid_forget()
        num_2.grid(row=0, column=2, padx=b_pad, pady=b_pad)
    elif button_count == 4:
        num_0.config(text=user_nums[0])
        num_1.config(text=user_nums[1])
        num_2.config(text=user_nums[2])
        num_3.config(text=user_nums[3])
        num_3.grid(row=1, column=0, padx=b_pad, pady=b_pad)
    elif button_count == 5:
        num_0.config(text=user_nums[0])
        num_1.config(text=user_nums[1])
        num_2.config(text=user_nums[2])
        num_3.config(text=user_nums[3])
        num_4.config(text=user_nums[4])
        num_4.grid(row=1, column=1, padx=b_pad, pady=b_pad)
    elif button_count == 6:
        num_0.config(text=user_nums[0])
        num_1.config(text=user_nums[1])
        num_2.config(text=user_nums[2])
        num_3.config(text=user_nums[3])
        num_4.config(text=user_nums[4])
        num_5.config(text=user_nums[5])
        num_5.grid(row=1, column=2, padx=b_pad, pady=b_pad)


def user_calc(b_val, ind_val):
    """Calculate the user result."""
    global nums_inp
    global user_nums
    global ind_0
    valid_entry = True
    produced = 0

    # Considers all possibilities of user input when entered
    if b_val == "enter":
        if nums_inp[0] != 0 and nums_inp[2] != 0:
            if nums_inp[1] == "+":
                produced = nums_inp[0] + nums_inp[2]
            elif nums_inp[1] == "-":
                if nums_inp[0] == nums_inp[2]:
                    valid_entry = False
                produced = abs(nums_inp[0] - nums_inp[2])
            elif nums_inp[1] == "*":
                produced = nums_inp[0] * nums_inp[2]
            elif nums_inp[1] == "/":
                if nums_inp[0] % nums_inp[2] == 0:
                    produced = int(nums_inp[0] / nums_inp[2])
                elif nums_inp[2] % nums_inp[0] == 0:
                    produced = int(nums_inp[2] / nums_inp[0])
                else:
                    valid_entry = False

            if valid_entry:
                user_nums.remove(nums_inp[0])
                user_nums.remove(nums_inp[2])
                user_nums.append(produced)
                user_history.append(user_nums.copy())
                modify_buttons_remove()
        else:
            pass
        oper_0.configure(background="white")
        oper_1.configure(background="white")
        oper_2.configure(background="white")
        oper_3.configure(background="white")
        num_0.configure(background="white")
        num_1.configure(background="white")
        num_2.configure(background="white")
        num_3.configure(background="white")
        num_4.configure(background="white")
        num_5.configure(background="white")
        nums_inp = [0, "!", 0]
    # Allows user to undo their move
    elif b_val == "undo":
        if len(user_history) != 1:
            del user_history[-1]
            user_nums = user_history[-1].copy()
            modify_buttons_add()
        oper_0.configure(background="white")
        oper_1.configure(background="white")
        oper_2.configure(background="white")
        oper_3.configure(background="white")
        num_0.configure(background="white")
        num_1.configure(background="white")
        num_2.configure(background="white")
        num_3.configure(background="white")
        num_4.configure(background="white")
        num_5.configure(background="white")
        nums_inp = [0, "!", 0]
        user_nums = user_history[-1].copy()
    elif b_val in ["+", "-", "*", "/"]:
        nums_inp[1] = b_val
        oper_0.configure(background="white")
        oper_1.configure(background="white")
        oper_2.configure(background="white")
        oper_3.configure(background="white")
        if b_val == "+":
            oper_0.configure(background="lightblue")
        elif b_val == "-":
            oper_1.configure(background="lightblue")
        elif b_val == "*":
            oper_2.configure(background="lightblue")
        else:
            oper_3.configure(background="lightblue")
    # Runs if the user pressed on any number or operator
    else:
        num_0.configure(background="white")
        num_1.configure(background="white")
        num_2.configure(background="white")
        num_3.configure(background="white")
        num_4.configure(background="white")
        num_5.configure(background="white")
        if nums_inp[0] == 0 or nums_inp[1] == "!" or ind_0 == ind_val:
            nums_inp[0] = b_val
            ind_0 = ind_val
            if ind_0 == 0:
                num_0.configure(background="lightblue")
            elif ind_0 == 1:
                num_1.configure(background="lightblue")
            elif ind_0 == 2:
                num_2.configure(background="lightblue")
            elif ind_0 == 3:
                num_3.configure(background="lightblue")
            elif ind_0 == 4:
                num_4.configure(background="lightblue")
            elif ind_0 == 5:
                num_5.configure(background="lightblue")
        else:
            nums_inp[2] = b_val
            ind_1 = ind_val
            if ind_0 == 0 or ind_1 == 0:
                num_0.configure(background="lightblue")
            if ind_0 == 1 or ind_1 == 1:
                num_1.configure(background="lightblue")
            if ind_0 == 2 or ind_1 == 2:
                num_2.configure(background="lightblue")
            if ind_0 == 3 or ind_1 == 3:
                num_3.configure(background="lightblue")
            if ind_0 == 4 or ind_1 == 4:
                num_4.configure(background="lightblue")
            if ind_0 == 5 or ind_1 == 5:
                num_5.configure(background="lightblue")


def user_complete():
    """User press the complete button."""
    global timer_end
    timer_end = True
    g_root.after_cancel(after_var)
    # Checks how close the user number is the target number
    if target_num - user_nums[0] == 0:
        exit_page("correct_number")
    elif abs(target_num - user_nums[0]) <= 50:
        exit_page("semi_correct_number")
    else:
        exit_page("lose_number")


def drop_timer():
    """Timer drop every 0.1 seconds."""
    global after_var
    global timer
    global timer_end
    timer = round(timer - 0.1, 2)
    timer_label.config(text=timer)
    # Ensures that the timer does not go into the negatives
    if timer < 0:
        exit_page("lose_timer")
    elif not timer_end:
        after_var = g_root.after(100, drop_timer)


def return_menu():
    """Return to the menu."""
    e_root.destroy()
    subprocess.run(["python", r"Python\11.3\menu\main_menu_tk.py"])


def go_to_game():
    """Go to the game again."""
    e_root.destroy()
    subprocess.run(["python", r"Python\11.3\game2\game2_main_countdown.py"])


def exit_page(win):
    """Run after the game is complete."""
    global e_root

    g_root.destroy()

    # Setting up the exit page root
    e_root = Tk(screenName="Game Over")
    e_root.title("Game Over")
    e_root.geometry("600x500+300+50")
    e_root.configure(background="Floral White")

    # Font setup for the titles and texts
    title_font = "Cambria"
    text_font = "Calibri"
    text_size = 9

    score = round(timer * (50 - abs(target_num - user_nums[0])))
    with open(r"Python\11.3\csv_files\user_scores.csv", "r",
              newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
        prev_high_score = int(rows[-1][2])
        new_high_score = max(int(rows[-1][2]), score)

    win_text = "Congratulations! You got the correct number!"
    score_txt = f"Your score is {score}."
    semi_win_text = "Nice try! At least you entered a decent number."
    high_score_text = "You also achieved a high score!"
    lose_text_time = "Game over! You ran out of time!"
    lose_text_num = "Game over! Your number was too far away!"

    # Checks the win conditions for each possibility
    if win == "correct_number" or win == "semi_correct_number":
        if win == "correct_number":
            Label(e_root, text="YOU WIN", font=(title_font, 36),
                  bg="Floral White").pack(pady=20)
            Label(e_root, text=win_text, wraplength=560, justify="left",
                  font=(text_font, text_size), bg="Floral White").pack()
            Label(e_root, text=score_txt, wraplength=560, justify="left",
                  font=(text_font, text_size), bg="Floral White").pack()
        elif win == "semi_correct_number":
            Label(e_root, text="SO CLOSE...", font=(title_font, 36),
                  bg="Floral White").pack(pady=20)
            Label(e_root, text=semi_win_text, wraplength=560, justify="left",
                  font=(text_font, text_size), bg="Floral White").pack()
            Label(e_root, text=score_txt, wraplength=560, justify="left",
                  font=(text_font, text_size), bg="Floral White").pack()
        if new_high_score > prev_high_score:
            Label(e_root, text=high_score_text, wraplength=560,
                  justify="left", font=(text_font, text_size),
                  bg="Floral White").pack()
            rows[-1][2] = new_high_score
            with open(r"Python\11.3\csv_files\user_scores.csv", "w",
                      newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
    else:
        Label(e_root, text="GAME OVER", font=(title_font, 36),
              bg="Floral White").pack(pady=20)
        if win == "lose_timer":
            Label(e_root, text=lose_text_time, wraplength=560, justify="left",
                  font=(text_font, text_size), bg="Floral White").pack()
        elif win == "lose_number":
            Label(e_root, text=lose_text_num, wraplength=560, justify="left",
                  font=(text_font, text_size), bg="Floral White").pack()

    scores_list = []
    for i in rows[1:]:
        scores_list.append([i[0], int(i[2])])

    # Gets a list of high scores if required
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

    # Creating the leaderboard
    Label(e_root, text="LEADERBOARD", font=(title_font, 24),
          bg="Floral White").pack(pady=20)
    leader_frame = Frame(e_root, bg="Floral White")
    leader_frame.pack()

    # This is important if there are not enough scores
    for i in high_score_list:
        if i[1] == 0:
            i[0] = "-"
            i[1] = "-"

    # Displaying the leaderboard using a grid
    first_user = Label(leader_frame, text=high_score_list[0][0],
                       font=(text_font, text_size), bg="Floral White")
    second_user = Label(leader_frame, text=high_score_list[1][0],
                        font=(text_font, text_size), bg="Floral White")
    third_user = Label(leader_frame, text=high_score_list[2][0],
                       font=(text_font, text_size), bg="Floral White")
    first_score = Label(leader_frame, text=high_score_list[0][1],
                        font=(text_font, text_size), bg="Floral White")
    second_score = Label(leader_frame, text=high_score_list[1][1],
                         font=(text_font, text_size), bg="Floral White")
    third_score = Label(leader_frame, text=high_score_list[2][1],
                        font=(text_font, text_size), bg="Floral White")

    l_padx = 20
    l_pady = 5
    first_user.grid(row=0, column=0, padx=l_padx, pady=l_pady)
    second_user.grid(row=1, column=0, padx=l_padx, pady=l_pady)
    third_user.grid(row=2, column=0, padx=l_padx, pady=l_pady)
    first_score.grid(row=0, column=1, padx=l_padx, pady=l_pady)
    second_score.grid(row=1, column=1, padx=l_padx, pady=l_pady)
    third_score.grid(row=2, column=1, padx=l_padx, pady=l_pady)

    # Bottom area asking user if they want to play again
    Label(e_root, text="PLAY AGAIN?", font=("Times New Roman", 24),
          bg="Floral White").pack(pady=20)
    replay_frame = Frame(e_root, width=560, bg="Floral White")
    replay_frame.pack()
    replay_button = Button(replay_frame, text="Yes", width=10,
                           font=(text_font, text_size), bg="Floral White",
                           command=go_to_game)
    menu_button = Button(replay_frame, text="No", width=10,
                         font=(text_font, text_size), bg="Floral White",
                         command=return_menu)
    replay_button.grid(row=0, column=0, padx=20)
    menu_button.grid(row=0, column=1, padx=20)


# Variables

nums_inp = [0, "!", 0]
numbers = get_numbers()
user_nums = numbers[:-1]
user_history = []
user_history.append(user_nums.copy())
timer = 60
timer_end = False
after_var = None

title_font = "Cambria"
text_font = "Calibri"

Label(g_root, text="COUNTDOWN", font=(title_font, 36),
      bg="Floral White").pack(pady=(20, 10))

# Elements on the top

top_items = Frame(g_root, bg="Floral White")
top_items.pack(pady=(0, 30))

target_number_txt = Label(top_items, text="Target Number", font=(
    text_font, 28), bg="Floral White")
timer_txt = Label(top_items, text="Timer", font=(
    text_font, 28), bg="Floral White")
target_number = Label(top_items, text=numbers[-1], borderwidth=5, font=(
    text_font, 28), bg="Floral White")
timer_label = Label(top_items, text=timer, font=(
    text_font, 28), bg="Floral White")

target_number_txt.grid(row=0, column=0, padx=30, pady=(30, 0))
timer_txt.grid(row=0, column=1, padx=30, pady=(30, 0))
target_number.grid(row=1, column=0, padx=30)
timer_label.grid(row=1, column=1, padx=30)

click_titles = Frame(g_root, bg="Floral White")
click_titles.pack()

user_numbers_txt = Label(click_titles, text="Your Numbers", font=(
    text_font, 28), bg="Floral White")
operators_txt = Label(click_titles, text="Operators", font=(
    text_font, 28), bg="Floral White")

# Items in the clickables area (Buttons and user inputs)

clickables = Frame(g_root, bg="Floral White")
clickables.pack()

user_numbers_txt.grid(row=0, column=0, padx=(50, 10))
operators_txt.grid(row=0, column=1, padx=(60, 80))

b_width = 7
b_height = 2
b_font_size = 12
b_pad = 10

num_0 = Button(clickables, text=user_nums[0], width=b_width, height=b_height,
               font=(text_font, b_font_size),
               command=lambda: user_calc(user_nums[0], 0),
               background="white")
num_1 = Button(clickables, text=user_nums[1], width=b_width,
               height=b_height, font=(text_font, b_font_size),
               command=lambda: user_calc(user_nums[1], 1), background="white")
num_2 = Button(clickables, text=user_nums[2], width=b_width, height=b_height,
               font=(text_font, b_font_size),
               command=lambda: user_calc(user_nums[2], 2), background="white")
num_3 = Button(clickables, text=user_nums[3], width=b_width, height=b_height,
               font=(text_font, b_font_size),
               command=lambda: user_calc(user_nums[3], 3), background="white")
num_4 = Button(clickables, text=user_nums[4], width=b_width, height=b_height,
               font=(text_font, b_font_size),
               command=lambda: user_calc(user_nums[4], 4), background="white")
num_5 = Button(clickables, text=user_nums[5], width=b_width, height=b_height,
               font=(text_font, b_font_size),
               command=lambda: user_calc(user_nums[5], 5), background="white")
oper_0 = Button(clickables, text="+", width=b_width, height=b_height,
                font=(text_font, b_font_size),
                command=lambda: user_calc("+", -1), background="white")
oper_1 = Button(clickables, text="-", width=b_width, height=b_height,
                font=(text_font, b_font_size),
                command=lambda: user_calc("-", -1), background="white")
oper_2 = Button(clickables, text="×", width=b_width, height=b_height,
                font=(text_font, b_font_size),
                command=lambda: user_calc("*", -1), background="white")
oper_3 = Button(clickables, text="÷", width=b_width, height=b_height,
                font=(text_font, b_font_size),
                command=lambda: user_calc("/", -1), background="white")
submit = Button(clickables, text="Enter", width=b_width, height=b_height,
                font=(text_font, b_font_size),
                command=lambda: user_calc("enter", -1), background="white")
undo = Button(clickables, text="Undo", width=b_width, height=b_height,
              font=(text_font, b_font_size),
              command=lambda: user_calc("undo", -1), background="white")
finish_button = Button(g_root, text="Finish!", width=2*b_width,
                       height=b_height, font=(text_font, b_font_size),
                       bg="LightBlue1", activebackground="LightBlue1",
                       command=lambda: user_complete())

# Clickables placed in a grid.

num_0.grid(row=0, column=0, padx=b_pad, pady=b_pad)
num_1.grid(row=0, column=1, padx=b_pad, pady=b_pad)
num_2.grid(row=0, column=2, padx=b_pad, pady=b_pad)
num_3.grid(row=1, column=0, padx=b_pad, pady=b_pad)
num_4.grid(row=1, column=1, padx=b_pad, pady=b_pad)
num_5.grid(row=1, column=2, padx=b_pad, pady=b_pad)
oper_0.grid(row=0, column=3, padx=b_pad, pady=b_pad)
oper_1.grid(row=0, column=4, padx=b_pad, pady=b_pad)
oper_2.grid(row=1, column=3, padx=b_pad, pady=b_pad)
oper_3.grid(row=1, column=4, padx=b_pad, pady=b_pad)
submit.grid(row=0, column=5, padx=b_pad, pady=b_pad)
undo.grid(row=1, column=5, padx=b_pad, pady=b_pad)

g_root.after(100, drop_timer)
g_root.mainloop()
