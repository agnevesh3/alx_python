#!/usr/bin/python3
"""This Module will rise an exception when area is not implemented"""


class BaseGeometry:
    """
    A class representing a basic geometry.

    Attributes:
        None

    Methods:
        area(): Raises an Exception indicating that area() is not implemented.
        integer_validator(name, value): Validates the given integer value.

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

    def integer_validator(self, name, value):
        """
        Validates the given integer value.

        Parameters:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Usage:
            This method is used to validate integer values for specific attributes in derived classes.
        """


"""This class inherits from BaseGeometry class, and has width and height as variables"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.width = width
        self.heigh = height
        if not isinstance(width, height, int):
            raise TypeError("{} must be an integer".format(width or height))
        if width <= 0:
            raise ValueError("{} must be greater than 0".format(width))
        if height <= 0:
            raise ValueError("{} must be greater than 0".format(height))
