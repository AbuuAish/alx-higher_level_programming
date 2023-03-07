#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    pos_val = -number
    last = pos_val % 10
    if (last > 5):
        print(f"Last digit of {number} is {last} and is greater than 5")
    elif (last == 0):
        print(f"Last digit of {number} is {last} and is zero")
    else:
        print(f"Last digit of {number} is {last} is less than 6 and not 0")
else:
    last = number % 10
    if (last > 5):
        print(f"Last digit of {number} is {last} and is greater than 5")
    elif (last == 0):
        print(f"Last digit of {number} is {last} and is zero")
    else:
        print(f"Last digit of {number} is {last} is less than 6 and not 0")
