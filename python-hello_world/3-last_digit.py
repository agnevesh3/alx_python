#!/usr/bin/env python3

import random

number = random.randint(-10000, 10000)
my_str = str(number)

# Check if my_str is not empty before accessing the last character
if my_str:
    last = int(my_str[-1])  # Convert the last digit to an integer

    if last > 5:
        print("Last digit of", number, "is", last, "and is greater than 5")
    elif last == 0:
        print("Last digit of", number, "is", last, "and is 0")
    else:
        print("Last digit of", number, "is", last, "and is less than 6 and not 0")
else:
    print("Error: 'my_str' is empty.")
