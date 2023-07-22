##The last digit
import random

number = random.randint(-10000, 10000)
my_str = str(number)
last = my_str[-1]
if int(last) > 5:
    print("Last digit of", number, "is", my_str[-1], "and is greater than 5")
elif int(last) == 0:
    print("Last digit of", number, "is", my_str[-1], "and is 0")
elif int(last) < 6 and int(last) != 0:
    print("Last digit of", number, "is", my_str[-1], "and is less than 6 and not 0")
