#!/usr/bin/python3
"""This is an empty class"""


class BaseGeometry:
    """It does not return anything"""

    pass


def custom_dir(obj):
    """Custom implementation of dir() to remove __init_subclass__ if present"""
    attributes = dir(obj)
    if "__init_subclass__" in attributes:
        attributes.remove("__init_subclass__")
    return attributes


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
