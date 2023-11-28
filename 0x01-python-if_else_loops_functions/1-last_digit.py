#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
if number > 5:
    print(f"Last digit of {number:d} is {number:d} and is greater than 5")
elif number == 0:
    print(f"Last digit of  {number:d} is {number:d} and is 0")
else:
    print(f"Last digit of {number:d} is {number:d} and is less than 6 and not 0")
