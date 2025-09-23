"""Tkinter code for game 2: Countdown"""

from tkinter import *
import random
import math

g_root = Tk(screenName="Game 2")
g_root.title("Game 2")
g_root.geometry("600x600")

# Functions

def GetNumbers():
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
        
        if attempt_target[0] <= 999:
            target_number = attempt_target[0]
            break
    
    num_set = list(num_set)
    num_set.append(target_number)
    return num_set

def UserCalc(b_val):
    global nums_inp
    if b_val == "enter":
        if nums_inp[0] != 0 and nums_inp[2] != 0:
            if nums_inp[1] == "+":
                print(nums_inp[0] + nums_inp[2])
            elif nums_inp[1] == "-":
                print(nums_inp[0] - nums_inp[2])
            elif nums_inp[1] == "*":
                print(nums_inp[0] * nums_inp[2])
            elif nums_inp[1] == "/":
                if nums_inp[0] % nums_inp[2] == 0:
                    print(int(nums_inp[0] / nums_inp[2]))
                elif nums_inp[2] % nums_inp[0] == 0:
                    print(int(nums_inp[2] / nums_inp[0]))
        else:
            print("Only 0 or 1 value entered")
        print(nums_inp)
        nums_inp = [0, "!", 0]
    elif b_val in ["+", "-", "*", "/"]:
        nums_inp[1] = b_val
    else:
        if nums_inp[0] == 0 or nums_inp[1] == "!" or b_val == nums_inp[0]:
            nums_inp[0] = b_val
        else:
            nums_inp[2] = b_val
    print(nums_inp)

# Variables
nums_inp = [0, "!", 0]
numbers = GetNumbers()
timer = 60

Label(g_root, text="COUNTDOWN", font=("Times New Roman", 36)).pack(
    pady=(20, 10))

# Elements on the top

top_items = Frame(g_root)
top_items.pack()

target_number_txt = Label(top_items, text="Target Number", font=(
    "Times New Roman", 28))
timer_txt = Label(top_items, text="Timer", font=(
    "Times New Roman", 28))
target_number = Label(top_items, text=numbers[-1], borderwidth=5, font=(
    "Times New Roman", 28))
timer = Label(top_items, text=timer, font=(
    "Times New Roman", 28))

target_number_txt.grid(row=0, column=0, padx=30, pady=(30, 0))
timer_txt.grid(row=0, column=1, padx=30, pady=(30, 0))
target_number.grid(row=1, column=0, padx=30)
timer.grid(row=1, column=1, padx=30)

click_titles = Frame(g_root)
click_titles.pack()

user_numbers_txt = Label(click_titles, text="Your Numbers", font=(
    "Times New Roman", 28))
operators_txt = Label(click_titles, text="Operators", font=(
    "Times New Roman", 28))

clickables = Frame(g_root)
clickables.pack()

user_numbers_txt.grid(row=0, column=0, padx=(30, 10))
operators_txt.grid(row=0, column=1, padx=(60, 80))

b_width = 7
b_height = 2
b_font_size = 12
b_pad = 10

num_0 = Button(clickables, text=numbers[0], width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc(numbers[0]))
num_1 = Button(clickables, text=numbers[1], width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc(numbers[1]))
num_2 = Button(clickables, text=numbers[2], width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc(numbers[2]))
num_3 = Button(clickables, text=numbers[3], width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc(numbers[3]))
num_4 = Button(clickables, text=numbers[4], width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc(numbers[4]))
num_5 = Button(clickables, text=numbers[5], width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc(numbers[5]))
oper_0 = Button(clickables, text="+", width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc("+"))
oper_1 = Button(clickables, text="-", width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc("-"))
oper_2 = Button(clickables, text="×", width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc("*"))
oper_3 = Button(clickables, text="÷", width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc("/"))
submit = Button(clickables, text="Enter", width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc("enter"))
undo = Button(clickables, text="Undo", width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size))

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

g_root.mainloop()
