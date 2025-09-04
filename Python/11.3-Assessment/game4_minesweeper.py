"""Python code for game 4: Minesweeper."""

import random

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
