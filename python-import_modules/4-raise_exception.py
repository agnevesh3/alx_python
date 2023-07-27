#!/usr/bin/python3
def raise_exception():
    try:
        result = print()
    except TypeError:
        result = print("Exception raised")
    return result
