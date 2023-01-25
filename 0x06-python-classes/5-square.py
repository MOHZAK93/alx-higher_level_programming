#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialize the square with a size.

        Args:
            size: size of square
        """
        self.__size = size

    @property
    def size(self):
        """Getter for size

        Return:
            valid size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size value

        Args:
            value: value of size
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes size of square

        Returns:
            area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
