"""
This module contains a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Parameters:
    obj (Any): The object to be checked.
    a_class (type): The class to compare against.

    Returns:
    bool: True if the object is an instance of a class that inherited from the specified class; otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
