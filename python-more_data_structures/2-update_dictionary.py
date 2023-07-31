#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Update or add key/value in a dictionary"""
    a_dictionary[key] = value
    return a_dictionary


def print_sorted_dictionary(my_dict):
    """Print sorted dictionary"""
    keys = sorted(my_dict.keys())
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))
