#!/usr/bin/env python3
def add(x, y):
    # add=x+y
    add = __import__("operator").add
    return add(x, y)


print(add(1, 2))
print(add(100, -2))
print(add(-100, -2))
print(add(0, 0))
