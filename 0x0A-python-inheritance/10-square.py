#!/usr/bin/python3
"""Square module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size):
        """Initializes a square size

        Args:
            size: size of square
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2
