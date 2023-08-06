#!/usr/bin/python3

"""
This module contains the BaseGeometry class.

The BaseGeometry class is an empty class that serves as a base for other geometry-related classes.
"""


class BaseGeometry:
    """
    A class representing a basic geometry.

    Attributes:
        None

    Methods:
        None

    Usage:
        This class can be inherited by other geometry-related classes to extend its functionality.
    """

    def __init__(self):
        pass


def custom_dir(obj):
    """
    Custom implementation of dir() to sort attributes alphabetically.

    Parameters:
        obj (object): The object for which to get the attributes.

    Returns:
        list: A sorted list of attributes of the object.
    """
    return sorted(dir(obj))


bg = BaseGeometry()
attributes = custom_dir(bg)

# Check the attributes and docstring
expected_output = [
    "__class__",
    "__delattr__",
    "__dict__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__gt__",
    "__hash__",
    "__init__",
    "__le__",
    "__lt__",
    "__module__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__setattr__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
    "__weakref__",
]

assert attributes == expected_output, f"Expected: {expected_output}\nGot: {attributes}"
