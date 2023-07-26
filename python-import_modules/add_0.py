#!/usr/bin/python3
from operator import __add__


def add(a, b):
    calc = __add__(a, b)
    print("{} + {} = {}".format((a), (b), (calc)))
    return calc


if __name__ == "__main__":
    a = 1
    b = 2
add(a, b)
