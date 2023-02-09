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
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
