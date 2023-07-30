#!/usr/bin/env python3
def no_c(my_string):
    my_list = []
    for i in my_string:
        my_list.append(i)
    if "c" in my_list:
        my_list.remove("c")
    elif "C" in my_list:
        my_list.remove("C")
    for i in my_list:
        result = print("{}".format(i), end="")
    return result
