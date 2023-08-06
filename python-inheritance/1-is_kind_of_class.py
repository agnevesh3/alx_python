#!/usr/bin/python3
"""
This module contains a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise false.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Parameters:
    obj (Any): The object to be checked.
    a_class (type): The class to compare against.

    Returns:
    bool: True if the object is an instance of the specified class; otherwise, False.
    The isinstance() function checks if obj is an instance of a_class or if it is an instance of a class that inherited from a_class.
    """
    return isinstance(obj, a_class)
