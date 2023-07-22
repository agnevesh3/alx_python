##Positive anything is better than negative nothing
import random

number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")
