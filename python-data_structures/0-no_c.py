#!/usr/bin/env python3
def no_c(my_string):
    my_list = []
    for i in my_string:
        my_list.append(i)
        for i in my_list:
            if i == "C" or i == "c":
                my_list.remove(i)
    for i in my_list:
        print("{}".format(i))
    return my_string
