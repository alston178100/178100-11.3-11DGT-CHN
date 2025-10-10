"""Tkinter code for game 2: Countdown"""

from tkinter import *
import random
import math

g_root = Tk(screenName="Game 2")
g_root.title("Game 2")
g_root.geometry("600x600+300+50")

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

def ModifyButtonsRemove():
    global temp_label_1
    global temp_label_2
    button_count = len(user_nums)
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
        temp_label_1 = Label(clickables, width=b_width, height=b_height)
        # Hard coded value b_pad + 5 due to strange width differences
        temp_label_1.grid(row=0, column=2, padx=b_pad+10, pady=b_pad)
        num_0.config(text=user_nums[0])
        num_1.config(text=user_nums[1])
    elif button_count == 1:
        num_1.grid_forget()
        temp_label_2 = Label(clickables, width=b_width, height=b_height)
        temp_label_2.grid(row=0, column=0, padx=b_pad+10, pady=b_pad)
        num_0.config(text=user_nums[0])
        num_0.grid(row=0, column=1, padx=b_pad, pady=b_pad)

def ModifyButtonsAdd():
    button_count = len(user_nums)
    print(button_count)
    if button_count == 2:
        num_0.config(text=user_nums[0])
        num_1.config(text=user_nums[1])
        temp_label_2.grid_forget()
        num_0.grid(row=0, column=0, padx=b_pad, pady=b_pad)
        num_1.grid(row=0, column=1, padx=b_pad, pady=b_pad)
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

def UserCalc(b_val, ind_val):
    global nums_inp
    global user_nums
    global ind_0
    valid_entry = True
    produced = 0

    if b_val == "enter":
        if nums_inp[0] != 0 and nums_inp[2] != 0:
            if nums_inp[1] == "+":
                produced = nums_inp[0] + nums_inp[2]
            elif nums_inp[1] == "-":
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
                print("Entered")
                print(user_history)
                ModifyButtonsRemove()
        else:
            print("Only 0 or 1 value entered")
        print(nums_inp)
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
    elif b_val == "undo":
        if len(user_history) != 1:
            del user_history[-1]
            user_nums = user_history[-1].copy()
            ModifyButtonsAdd()
            print("Deleted")
            print(user_history)
            print(user_nums)
        else:
            print("Nothing to undo")
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
            print(ind_0)
            print(ind_1)
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

# Variables
nums_inp = [0, "!", 0]
numbers = GetNumbers()
user_nums = numbers[:-1]
user_history = []
user_history.append(user_nums.copy())
print(user_history)
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

num_0 = Button(clickables, text=user_nums[0], width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc(user_nums[0], 0), background="white")
num_1 = Button(clickables, text=user_nums[1], width=b_width, 
               height=b_height, font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc(user_nums[1], 1), background="white")
num_2 = Button(clickables, text=user_nums[2], width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc(user_nums[2], 2), background="white")
num_3 = Button(clickables, text=user_nums[3], width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc(user_nums[3], 3), background="white")
num_4 = Button(clickables, text=user_nums[4], width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc(user_nums[4], 4), background="white")
num_5 = Button(clickables, text=user_nums[5], width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc(user_nums[5], 5), background="white")
oper_0 = Button(clickables, text="+", width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc("+", -1), background="white")
oper_1 = Button(clickables, text="-", width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc("-", -1), background="white")
oper_2 = Button(clickables, text="×", width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc("*", -1), background="white")
oper_3 = Button(clickables, text="÷", width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc("/", -1), background="white")
submit = Button(clickables, text="Enter", width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc("enter", -1), background="white")
undo = Button(clickables, text="Undo", width=b_width, height=b_height, 
               font=("Times New Roman", b_font_size), 
               command=lambda:UserCalc("undo", -1), background="white")

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
