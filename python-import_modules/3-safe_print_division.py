#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        division = None
        return division
    else:
        return division
    finally:
        print("Inside result:", division)
    print("{} / {} = {}".format(a, b, division))
