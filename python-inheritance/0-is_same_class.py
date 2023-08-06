#!/usr/bin/python3
# type_checker.py

"""
This module defines the type of attribute.


Attributes:
    obj, and a_class.
"""


class TypeChecker:
    """
    A class to check if an object is exactly an instance of a specified class.

    This class provides a method, is_same_class, that checks if the given object is an instance
    of the specified class. It uses the __class__ attribute of the object to get its class and
    compares it with the specified class to determine if they match.
    """

    def is_same_class(self, obj, a_class):
        """
        Check if the given object is exactly an instance of the specified class.

        Parameters:
            obj (object): The object to be checked.
            a_class (class): The class to compare with.

        Returns:
            bool: True if the object is an instance of the specified class; otherwise, False.

        Examples:
            >>> checker = TypeChecker()
            >>> a = 1
            >>> checker.is_same_class(a, int)
            True

            >>> checker.is_same_class(a, float)
            False

            >>> checker.is_same_class(a, object)
            True

        Note:
            This method uses the __class__ attribute of the object to check if it is an instance of the
            specified class. It returns True if the object's class is the same as the specified class.
            If the object is not an instance of the specified class, it returns False.
        """
        return obj.__class__ is a_class
