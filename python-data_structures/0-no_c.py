#!/usr/bin/env python3
def no_c(my_string):
    my_list = []
    for i in my_string:
        if i.lower() != "c":  # Convert the character to lowercase for comparison
            my_list.append(i)
    for i in my_list:
        print("{}".format(i), end="")


no_c("School")
