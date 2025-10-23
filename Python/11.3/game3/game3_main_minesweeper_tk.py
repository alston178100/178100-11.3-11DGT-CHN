"""Tkinter code for game 3: Minesweeper."""

from tkinter import Tk, Button, Label, Frame, DISABLED, CENTER
import random
import subprocess
import csv

g_root = Tk(screenName="Game 3")
g_root.title("Game 3")
g_root.geometry("600x600+300+50")
g_root.configure(bg="Floral White")


# Functions

def get_grid():
    """Find the grid for minesweeper."""
    sweeper_li = []
    for i in range(16):
        sweeper_li.append([0] * 16)

    mines_li = []
    for i in range(40):
        x = random.randint(0, 15)
        y = random.randint(0, 15)
        while (x, y) in mines_li:
            x = random.randint(0, 15)
            y = random.randint(0, 15)
        mines_li.append((x, y))

    # Creates the mines grid
    for i in mines_li:
        row = i[0]
        col = i[1]
        sweeper_li[row][col] = 9
        if row != 0:
            if sweeper_li[row-1][col] != 9:
                sweeper_li[row-1][col] += 1
            if col != 0:
                if sweeper_li[row-1][col-1] != 9:
                    sweeper_li[row-1][col-1] += 1
            if col != 15:
                if sweeper_li[row-1][col+1] != 9:
                    sweeper_li[row-1][col+1] += 1
        if row != 15:
            if sweeper_li[row+1][col] != 9:
                sweeper_li[row+1][col] += 1
            if col != 0:
                if sweeper_li[row+1][col-1] != 9:
                    sweeper_li[row+1][col-1] += 1
            if col != 15:
                if sweeper_li[row+1][col+1] != 9:
                    sweeper_li[row+1][col+1] += 1
        if col != 0:
            if sweeper_li[row][col-1] != 9:
                sweeper_li[row][col-1] += 1
        if col != 15:
            if sweeper_li[row][col+1] != 9:
                sweeper_li[row][col+1] += 1

    for i in sweeper_li:
        print(i)
    return sweeper_li


def reveal_lost(r, c):
    """Reveal mines when the game is lost."""
    global game_lost
    game_lost = True
    # Revealing the bomb through looping
    for i in range(16):
        for j in range(16):
            globals()["button_" + str(i) + "_" + str(j)].config(state=DISABLED)
            globals()["button_" + str(i) + "_" + str(j)
                      ].unbind("<Button-2>")
            globals()["button_" + str(i) + "_" + str(j)
                      ].unbind("<Button-3>")
            if sweeper_grid[i][j] == 9 and (i, j) != (r, c):
                globals()["button_" + str(i) + "_" + str(j)].config(
                    text="💣", background="snow", disabledforeground="black")
    # Cancelling the timer allows for no errors
    g_root.after_cancel(after_var)
    g_root.after(2000, lambda: exit_page("lose_mine"))


def win_change(row):
    """Make the grid green when it is cleared."""
    for i in range(16):
        globals()["button_" + str(row) + "_" + str(i)
                  ].config(bg="DarkSeaGreen1", disabledforeground="black")
        # Makes sure that bombs are revealed at the end
        if sweeper_grid[row][i] == 9:
            globals()["button_" + str(row) + "_" + str(i)].config(
                text="💣")
    if row == 15:
        if timer_win:
            g_root.after(1000, lambda: exit_page("clear"))
        else:
            g_root.after(1000, lambda: exit_page("lose_timer"))
    else:
        # Creates the animation
        g_root.after(50, win_change(row+1))


def reveal_win():
    """Unbind all of the buttons so they cannot get flagged."""
    for i in range(16):
        for j in range(16):
            globals()["button_" + str(i) + "_" + str(j)
                      ].unbind("<Button-3>")
    win_change(0)


def reveal_button(r, c):
    """Reveal the button depending on their number."""
    global safe_squares_revealed
    if not flag_placed[r][c]:
        globals()["button_" + str(r) + "_" + str(c)
                  ].config(state=DISABLED, background="snow")
        revealed[r][c] = 1
        if sweeper_grid[r][c] == 0:
            # Recursion allows all adjacent zero squares to be removed
            surrounded_squares = []
            surrounded_squares.append((r-1, c-1))
            surrounded_squares.append((r-1, c))
            surrounded_squares.append((r-1, c+1))
            surrounded_squares.append((r, c-1))
            surrounded_squares.append((r, c+1))
            surrounded_squares.append((r+1, c-1))
            surrounded_squares.append((r+1, c))
            surrounded_squares.append((r+1, c+1))
            for i in surrounded_squares:
                if i[0] >= 0 and i[1] >= 0 and i[0] <= 15 and i[1] <= 15:
                    if not revealed[i[0]][i[1]]:
                        reveal_button(i[0], i[1])
            safe_squares_revealed += 1
        # The selected grid has a number
        elif sweeper_grid[r][c] != 9:
            globals()["button_" + str(r) + "_" + str(c)].config(
                text=sweeper_grid[r][c],
                disabledforeground=colours[sweeper_grid[r][c]-1])
            safe_squares_revealed += 1
        # The selected grid is a bomb
        else:
            globals()["button_" + str(r) + "_" + str(c)].config(
                text="💣", background="red", disabledforeground="black")
            g_root.after(10, lambda: reveal_lost(r, c))
        # When all safe squares have been revealed
        if safe_squares_revealed == 216:
            g_root.after_cancel(after_var)
            g_root.after(10, reveal_win)


def change_flag(r, c):
    """Place or remove a flag when there is a right click."""
    global flags_left
    button_var = "button_" + str(r) + "_" + str(c)
    if not revealed[r][c]:
        # Placing and removing flags system
        if flag_placed[r][c]:
            globals()[button_var].config(text="", padx=0, pady=0)
            flag_placed[r][c] = 0
            flags_left += 1
        else:
            globals()[button_var].config(text="🚩",
                                         compound=CENTER, padx=0, pady=0)
            flag_placed[r][c] = 1
            flags_left -= 1
        flags_left_text.config(text=flags_left)


def chording_func(r, c):
    """Run when the user middle clicks and wants to do chording."""
    global flag_placed
    global sweeper_grid
    surrounded_squares = []
    surrounded_squares.append((r-1, c-1))
    surrounded_squares.append((r-1, c))
    surrounded_squares.append((r-1, c+1))
    surrounded_squares.append((r, c-1))
    surrounded_squares.append((r, c+1))
    surrounded_squares.append((r+1, c-1))
    surrounded_squares.append((r+1, c))
    surrounded_squares.append((r+1, c+1))
    for i in surrounded_squares.copy():
        if i[0] < 0 or i[1] < 0 or i[0] > 15 or i[1] > 15:
            surrounded_squares.remove(i)
    surrounded_flags = 0
    for i in surrounded_squares:
        if flag_placed[i[0]][i[1]]:
            surrounded_flags += 1
    # Reveals the surrounding squares
    if sweeper_grid[r][c] == surrounded_flags and revealed[r][c]:
        for i in surrounded_squares:
            if not revealed[i[0]][i[1]]:
                reveal_button(i[0], i[1])


def return_menu():
    """Return to the menu."""
    e_root.destroy()
    subprocess.run(["python", r"Python\11.3\menu\main_menu_tk.py"])


def go_to_game():
    """Go back to the game again."""
    e_root.destroy()
    subprocess.run(["python",
                    r"Python\11.3\game3\game3_main_minesweeper_tk.py"])


def exit_page(win):
    """Run when the game is completed."""
    global e_root
    global title_font
    text_font = "Calibri"
    text_size = 11

    g_root.destroy()

    # New root created for game over
    e_root = Tk(screenName="Game Over")
    e_root.title("Game Over")
    e_root.geometry("600x500+300+50")
    e_root.configure(background="Floral White")

    score = 300 - timer
    with open(r"Python\11.3\csv_files\user_scores.csv", "r",
              newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
        prev_high_score = int(rows[-1][3])
        new_high_score = max(int(rows[-1][3]), score)

    win_text = "Congratulations! You cleared the board!"
    score_txt = f"Your score is {score}."
    high_score_text = "You also achieved a high score!"
    lose_text_time = "Unlucky! You spent too long! At least you " \
        "cleared the board..."
    lose_text_mine = "Game over! You clicked on a mine!"

    # The user cleared the board
    if win == "clear":
        Label(e_root, text="YOU WIN", font=(title_font, 36),
              background="Floral White").pack(pady=20)
        Label(e_root, text=win_text, wraplength=560, justify="left",
              font=(text_font, text_size), background="Floral White").pack()
        Label(e_root, text=score_txt, wraplength=560, justify="left",
              font=(text_font, text_size), background="Floral White").pack()
        if new_high_score > prev_high_score:
            Label(e_root, text=high_score_text, wraplength=560,
                  justify="left", font=(text_font, text_size),
                  background="Floral White").pack()
            rows[-1][3] = new_high_score
            with open(r"Python\11.3\csv_files\user_scores.csv", "w",
                      newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
    else:
        # User either took too long or lost due to clicking on a mine
        Label(e_root, text="GAME OVER", font=(title_font, 36),
              background="Floral White").pack(pady=20)
        if win == "lose_timer":
            Label(e_root, text=lose_text_time, wraplength=560,
                  justify="left", font=(text_font, text_size),
                  background="Floral White").pack()
        elif win == "lose_mine":
            Label(e_root, text=lose_text_mine, wraplength=560,
                  justify="left", font=(text_font, text_size),
                  background="Floral White").pack()

    # Checking for high score
    scores_list = []
    for i in rows[1:]:
        scores_list.append([i[0], int(i[3])])
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

    # Loading the leaderboard
    Label(e_root, text="LEADERBOARD", font=(title_font, 24),
          background="Floral White").pack(pady=20)
    leader_frame = Frame(e_root, background="Floral White")
    leader_frame.pack()

    # This exists if there is not enough scores
    for i in high_score_list:
        if i[1] == 0:
            i[0] = "-"
            i[1] = "-"

    first_user = Label(leader_frame, text=high_score_list[0][0],
                       font=(text_font, text_size), background="Floral White")
    second_user = Label(leader_frame, text=high_score_list[1][0],
                        font=(text_font, text_size), background="Floral White")
    third_user = Label(leader_frame, text=high_score_list[2][0],
                       font=(text_font, text_size), background="Floral White")
    first_score = Label(leader_frame, text=high_score_list[0][1],
                        font=(text_font, text_size), background="Floral White")
    second_score = Label(leader_frame, text=high_score_list[1][1],
                         font=(text_font, text_size),
                         background="Floral White")
    third_score = Label(leader_frame, text=high_score_list[2][1],
                        font=(text_font, text_size), background="Floral White")

    l_padx = 20
    l_pady = 5
    first_user.grid(row=0, column=0, padx=l_padx, pady=l_pady)
    second_user.grid(row=1, column=0, padx=l_padx, pady=l_pady)
    third_user.grid(row=2, column=0, padx=l_padx, pady=l_pady)
    first_score.grid(row=0, column=1, padx=l_padx, pady=l_pady)
    second_score.grid(row=1, column=1, padx=l_padx, pady=l_pady)
    third_score.grid(row=2, column=1, padx=l_padx, pady=l_pady)

    # User can play again at the bottom
    Label(e_root, text="PLAY AGAIN?", font=(title_font, 24),
          background="Floral White").pack(pady=20)
    replay_frame = Frame(e_root, width=560, background="Floral White")
    replay_frame.pack()
    replay_button = Button(replay_frame, text="Yes", width=10,
                           command=go_to_game, font=(text_font, text_size),
                           background="Floral White")
    menu_button = Button(replay_frame, text="No", width=10,
                         command=return_menu, font=(text_font, text_size),
                         background="Floral White")
    replay_button.grid(row=0, column=0, padx=20)
    menu_button.grid(row=0, column=1, padx=20)


# This function is necessary since i and j are dynamic variables

def edit_button_commands(r, c):
    """Edit the commands for grid buttons."""
    globals()["button_" + str(r) + "_" + str(c)
              ].config(command=lambda: reveal_button(r, c))
    globals()["button_" + str(r) + "_" + str(c)
              ].bind("<Button-2>", lambda x: chording_func(r, c))
    globals()["button_" + str(r) + "_" + str(c)
              ].bind("<Button-3>", lambda x: change_flag(r, c))


def increase_timer():
    """Run every second to keep track of time."""
    global after_var
    global timer_win
    global timer
    timer += 1
    timer_label.config(text=timer)
    # Timer continues until game is over
    if timer == 300:
        timer_win = False
    if not game_lost:
        after_var = g_root.after(1000, increase_timer)


# Variables

colours = ["blue1", "green4", "red", "darkorchid4", "brown4", "cyan4",
           "black", "orange2"]
revealed = []
flag_placed = []
for i in range(16):
    revealed.append([0] * 16)
    flag_placed.append([0] * 16)
safe_squares_revealed = 0
timer = 0
game_lost = False
timer_win = True
after_var = None

sweeper_grid = get_grid()

# Minesweeper Tkinter set up

title_font = "Cambria"
upper_font = "Calibri"

Label(g_root, text="MINESWEEPER", font=(title_font, 36),
      bg="Floral White").pack(pady=(20, 10),)

flags_left = 40
upper_frame = Frame(g_root, bg="Floral White")
upper_frame.pack(pady=10)

Label(upper_frame, text="Flags Left", bg="Floral White",
      font=(upper_font, 28)).grid(row=0, column=0, padx=30)
flags_left_text = Label(upper_frame, text=flags_left, bg="Floral White",
                        font=(upper_font, 28))
flags_left_text.grid(row=1, column=0, padx=30)

Label(upper_frame, text="Timer", bg="Floral White",
      font=(upper_font, 28)).grid(row=0, column=1, padx=30)
timer_label = Label(upper_frame, text=timer, bg="Floral White",
                    font=(upper_font, 28))
timer_label.grid(row=1, column=1, padx=30)

mines_frame = Frame(g_root, width=350, height=350)
mines_frame.grid_propagate(False)
mines_frame.pack()

for i in range(16):
    # Creating the mines with a button system
    mines_frame.rowconfigure(i, weight=1)
    mines_frame.columnconfigure(i, weight=1)
    for j in range(16):
        # Defines a variable in terms of a string (Prevents hardcoding)
        var_str = "button_" + str(i) + "_" + str(j)
        globals()[var_str] = Button(mines_frame, width=2, height=2,
                                    borderwidth=0.5, relief="ridge",
                                    bg="LightBlue1", highlightthickness=0,
                                    activebackground="LightBlue2")
        edit_button_commands(i, j)
        globals()[var_str].grid(row=i, column=j, sticky="nesw")

# Searches toward the middle
break_i_loop = False
for i in range(16):
    for j in range(6):
        if sweeper_grid[8-i][10-j] == 0:
            # Middle search to ensure the correct square is highlighted
            if i > 8:
                globals()["button_" + str(16-abs(8-i)) + "_" + str(10-j)
                          ].config(background="Yellow")
                temp_button_coords = (16-abs(8-i), 10-j)
            else:
                globals()["button_" + str(8-i) + "_" + str(10-j)
                          ].config(background="Yellow")
                temp_button_coords = (8-i, 10-j)
            break_i_loop = True
            break
    if break_i_loop:
        break

# Backup if the above doesn't work (Super low chance)
while not break_i_loop:
    x_coord = random.randint(0, 15)
    y_coord = random.randint(0, 15)
    if sweeper_grid[x_coord][y_coord] == 0:
        globals()["button_" + str(x_coord) + "_" + str(y_coord)
                  ].config(background="Yellow")
        temp_button_coords = (x_coord, y_coord)
        break_i_loop = True

g_root.after(1000, increase_timer)
g_root.mainloop()
