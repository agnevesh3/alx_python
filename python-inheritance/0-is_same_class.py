#!/usr/bin/python3
"""
    Check if the given object is exactly an instance of the specified class.

    Parameters:
        obj (object): The object to be checked.
        a_class (class): The class to compare with.

    Returns:
        bool: True if the object is an instance of the specified class; otherwise, False.
    """"
def is_same_class(obj, a_class):
    
    """"

    Examples:
        is_same_class(5, int)
        True

        is_same_class("hello", str)
        True

        is_same_class(5, float)
        False

    Note:
        The function does not support checking against built-in types that have type aliases.
    """
    return type(obj) is a_class
