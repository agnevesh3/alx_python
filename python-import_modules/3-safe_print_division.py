#!/usr/bin/python3
from __future__ import division


def safe_print_division(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        division = None
    finally:
        print("Inside result:", division)
        print("{} / {} = {}".format(a, b, division))


a = 10
b = 2
result = safe_print_division(a, b)
