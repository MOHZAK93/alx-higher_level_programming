#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialize the square with a size.

        Args:
            size: size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes size of square

        Returns area of square
        """
        return self.__size * self.__size
