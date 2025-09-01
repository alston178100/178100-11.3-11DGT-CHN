""""Python code for game 2: Countdown."""

import random
import math

# Initialisng the list of numbers for user

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
