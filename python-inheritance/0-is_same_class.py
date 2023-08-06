#!/usr/bin/python3


class TypeChecker:
    """
    A class to check if an object is exactly an instance of a specified class.

    Example usage:
    >>> checker = TypeChecker()
    >>> a = 1
    >>> if checker.is_same_class(a, int):
    ...     print("{} is an instance of the class {}".format(a, int.__name__))
    ...
    1 is an instance of the class int

    >>> if checker.is_same_class(a, float):
    ...     print("{} is an instance of the class {}".format(a, float.__name__))
    ...
    (no output since a is not an instance of float)

    >>> if checker.is_same_class(a, object):
    ...     print("{} is an instance of the class {}".format(a, object.__name__))
    ...
    (no output since a is not an instance of object)
    """

    def is_same_class(self, obj, a_class):
        """
        Check if the given object is exactly an instance of the specified class.

        Parameters:
            obj (object): The object to be checked.
            a_class (class): The class to compare with.

        Returns:
            bool: True if the object is an instance of the specified class; otherwise, False.
        """
        return obj.__class__ is a_class
