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


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
        None

    Methods:
        __init__(self, width, height): Initializes a Rectangle instance with given width and height.
        area(): Calculates and returns the area of the rectangle.

    Usage:
        This class can be used to represent rectangles with positive integer width and height.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with given width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.width = width
        self.height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height
