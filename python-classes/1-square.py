"""
This module defines the Square class.

The Square class represents a square with a given size.

Attributes:
    __size (int): The size of the square.
"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer.")
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
