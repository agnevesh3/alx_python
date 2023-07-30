#!/usr/bin/env python3
def no_c(my_string):
    my_list = []
    for i in my_string:
        my_list.append(i)
    if "C" in my_list:
        my_string = my_list.remove("C")
        if "c" in my_list:
            my_string = my_list.remove("c")
    for i in my_list:
        print("{}".format(i), end="")
    return my_string
