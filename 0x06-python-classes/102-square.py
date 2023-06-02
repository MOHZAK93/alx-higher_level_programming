#!/usr/bin/python3
"""A class that inherits a square"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initializes a square"""

        self.size = size

    def __eq__(self, comp):
        """Equality comparison of square"""
        if type(comp) is Square:
            return self.area() == comp.area()

    def __ne__(self, comp):
        """Nonequality comparison of Square"""
        if type(comp) is Square:
            return self.area() != comp.area()

    def __lt__(self, comp):
        """Less than comparison of Square"""
        if type(comp) is Square:
            return self.area() < comp.area()

    def __gt__(self, comp):
        """Greater than comparison of Square"""
        if type(comp) is Square:
            return self.area() > comp.area()

    def __ge__(self, comp):
        """Greater than or equal comparison of Square"""
        if type(comp) is Square:
            return self.area() >= comp.area()

    def __le__(self, comp):
        """Less than or equal comparison of Square"""
        if type(comp) is Square:
            return self.area() <= comp.area()

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square"""
        if not isinstance(value, int) and not isinstance(value, float):
            raise ValueError("size must be a number")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns area of square"""
        return self.__size ** 2
