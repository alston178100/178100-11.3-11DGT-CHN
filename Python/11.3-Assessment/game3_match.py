"""Python code for game 3: Match the brainrot."""

import random

# Setting up screen display

characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

selection_list = set()

while len(selection_list) != 12:
    selection_list.add(characters[random.randint(0, 25)])

selection_list = list(selection_list)

dict_count = {}
for i in range(12):
    dict_count[selection_list[i]] = 0

screen_display = []
for i in range(3):
    screen_display.append([0] * 8)

for i in range(3):
    for j in range(8):
        element = selection_list[random.randint(0, len(selection_list) - 1)]
        dict_count[element] += 1
        screen_display[i][j] = element
        if dict_count[element] == 2:
            selection_list.remove(element)

for i in screen_display:
    print(i)
