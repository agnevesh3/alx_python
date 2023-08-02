#!/usr/bin/python3
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

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Parameters:
            size (int): The size of the square.
        """
        self.__size = size
