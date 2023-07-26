#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        division = a / b
    except ZeroDivisionError:
        division = None
    except NameError:
        division = None
    finally:
        print("Inside result:", division)
        print("{} / {} = {}".format(a, b, division))
