#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Check if the given object is exactly an instance of the specified class.

    Parameters:
        obj (object): The object to be checked.
        a_class (class): The class to compare with.

    Returns:
        bool: True if the object is an instance of the specified class; otherwise, False.

    Examples:
        >>> a = 1
        >>> is_same_class(a, int)
        True

        >>> is_same_class(a, float)
        False

        >>> is_same_class(a, object)
        True

    Note:
        This function uses the __class__ attribute of the object to check if it is an instance of the
        specified class. It returns True if the object's class is the same as the specified class.
        If the object is not an instance of the specified class, it returns False.
    """
    return obj.__class__ is a_class
