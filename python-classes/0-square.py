#!/usr/bin/python3
class Square:
    """this block will declare the size of square"""

    def __init__(self, size):
        """A simple module that return the size of a square"""
        try:
            self.__size = size
        except Exception as e:
            print(e)
