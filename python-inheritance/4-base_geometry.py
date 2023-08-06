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
        area(): Raises an Exception indicating that area() is not implemented.

    Usage:
        This class can be inherited by other geometry-related classes to extend its functionality.
    """

    def area(self):
        """
        Raises an Exception indicating that area() is not implemented.

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
