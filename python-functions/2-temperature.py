#!/usr/bin/env python3
def convert_to_celsius(fahrenheit):
    # convert_to_celsius = __import__("operator").
    convert_to_celsius = (float(fahrenheit) - 32) * (5 / 9)
    return round(convert_to_celsius, 2)


# print(convert_to_celsius(459.67))
# print(convert_to_celsius(-40))
# print(convert_to_celsius(-459.67))
# print(convert_to_celsius(32))
