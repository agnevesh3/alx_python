#!/usr/bin/env python3
def my_power(x, y):
    try:
        pow = __import__("1-power").pow
    except:
        a = x**y
        return a


# print(pow(2, 2))
# print(pow(98, 2))
# print(pow(98, 0))
# print(pow(100, -2))
# print(pow(-4, 5))
