"""Tkinter code for game 4: Minesweeper"""

from tkinter import *
import random

g_root = Tk(screenName="Game 4")
g_root.title("Game 4")
g_root.geometry("600x600")

# Functions

def GetGrid():
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

def RevealLost(r, c):
    for i in range(16):
        for j in range(16):
            globals()["button_" + str(i) + "_" + str(j)].config(state=DISABLED)
            if sweeper_grid[i][j] == 9 and (i, j) != (r, c):
                bg_img = Label(mines_frame, image=PhotoImage(width=18, height=18), 
                                background="white")
                bg_img.grid(row=i, column=j)
                Label(mines_frame, text="💣", 
                        background="white").grid(row=i, column=j)
                bg_img = Label(mines_frame, image=PhotoImage(width=18, height=18), 
                                background="white")

def RevealButton(r, c):
    global safe_squares_revealed
    globals()["button_" + str(temp_button_coords[0]) + 
              "_" + str(temp_button_coords[1])].config(
                  background="SystemButtonFace")
    if not flag_placed[r][c]:
        globals()["button_" + str(r) + "_" + str(c)].config(state=DISABLED)
        bg_img = Label(mines_frame, image=PhotoImage(width=18, height=18), 
                        background="white")
        bg_img.grid(row=r, column=c)
        revealed[r][c] = 1

        if sweeper_grid[r][c] == 0:
            Label(mines_frame, background="white").grid(row=r, column=c)
            # Recursion allows all adjacent zero squares to be removed
            if r != 0:
                if not revealed[r-1][c]:
                    RevealButton(r-1, c)
                if c != 0:
                    if not revealed[r-1][c-1]:
                        RevealButton(r-1, c-1)
                if c != 15:
                    if not revealed[r-1][c+1]:
                        RevealButton(r-1, c+1)
            if r != 15:
                if not revealed[r+1][c]:
                    RevealButton(r+1, c)
                if c != 0:
                    if not revealed[r+1][c-1]:
                        RevealButton(r+1, c-1)
                if c != 15:
                    if not revealed[r+1][c+1]:
                        RevealButton(r+1, c+1)
            if c != 0:
                if not revealed[r][c-1]:
                    RevealButton(r, c-1)
            if c != 15:
                if not revealed[r][c+1]:
                    RevealButton(r, c+1)
            safe_squares_revealed += 1
        elif sweeper_grid[r][c] != 9:
            Label(mines_frame, text=sweeper_grid[r][c], 
                  background="white", fg=colours[sweeper_grid[r][c]-1]
                  ).grid(row=r, column=c)
            safe_squares_revealed += 1
        else:
            bg_img = Label(mines_frame, image=PhotoImage(width=19, height=19), 
                        background="red")
            bg_img.grid(row=r, column=c)
            Label(mines_frame, text="💣", background="red"
                  ).grid(row=r, column=c)
            g_root.after(10, lambda: RevealLost(r, c))
        if safe_squares_revealed == 216:
            print("WIN")

def ChangeFlag(r, c):
    global flags_left
    if flag_placed[r][c]:
        globals()["button_" + str(r) + "_" + str(c)].config(text="", padx=0, 
                                                            pady=0)
        flag_placed[r][c] = 0
        flags_left += 1
    else:
        globals()["button_" + str(r) + "_" + str(c)
                  ].config(text="🚩", compound=CENTER, padx=0, pady=0,
                           font=("Arial", 9))
        flag_placed[r][c] = 1
        flags_left -= 1
    flags_left_text.config(text=flags_left)

# This function is necessary since i and j are dynamic variables
def EditButtonCommands(r, c):
    globals()["button_" + str(r) + "_" + str(c)
              ].config(command=lambda: RevealButton(r, c))
    globals()["button_" + str(r) + "_" + str(c)
              ].bind("<Button-3>", lambda x: ChangeFlag(r, c))

# Variables

colours = ["blue1", "green4", "red", "darkorchid4", "brown4", "cyan4", 
           "black", "orange2"]
revealed = []
flag_placed = []
for i in range(16):
    revealed.append([0] * 16)
    flag_placed.append([0] * 16)
safe_squares_revealed = 0

sweeper_grid = GetGrid()

# Minesweeper Tkinter set up

Label(g_root, text="MINESWEEPER", font=("Times New Roman", 36)).pack(
    pady=(20, 10))

flags_left = 40
upper_frame = Frame(g_root)
upper_frame.pack(pady=10)

Label(upper_frame, text="Flags Left").grid(row=0, column=0)
flags_left_text = Label(upper_frame, text=flags_left)
flags_left_text.grid(row=1, column=0)

mines_frame = Frame(g_root, width=150, height=150)
mines_frame.pack()
pixel_img = PhotoImage(width=20, height=20)

for i in range(16):
    for j in range(16):
        # Defines a variable in terms of a string (Prevents hardcoding)
        var_str = "button_" + str(i) + "_" + str(j)
        globals()[var_str] = Button(mines_frame, image=pixel_img, 
                                    highlightthickness=0)
        EditButtonCommands(i, j)
        globals()[var_str].grid(row=i, column=j)

# Searches toward the middle
break_i_loop = False
pixel_img_2 = PhotoImage(width=20, height=20)
for i in range(16):
    for j in range(6):
        if sweeper_grid[8-i][10-j] == 0:
            if i > 8:
                globals()["button_" + str(16-abs(8-i)) + "_" + str(10-j)
                          ].config(image=pixel_img_2)
                temp_button_coords = (16-abs(8-i), 10-j)
            else:
                globals()["button_" + str(8-i) + "_" + str(10-j)
                          ].config(background="yellow")
                temp_button_coords = (8-i, 10-j)
            break_i_loop = True
            break
    if break_i_loop:
        break

g_root.mainloop()
