#!/usr/bin/python3
"""A class that defines a Square"""


class Square():
    """Defines a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instializes a Square with size and position"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of Square"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrives position of Square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets position of Square"""

        if (
                not isinstance(value, tuple)
                or type(value[0]) is not int
                or type(value[1]) is not int
                or len(value) != 2
                or value[0] < 0
                or value[1] < 0
                ):
            raise TypeError("size must be an integer")
        else:
            self.__position = value

    def area(self):
        """Computes area of Square"""

        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with character #"""

        for i in range(self.__position[1]):
            print()
        for x in range(self.__size):
            for j in range(self.__position[0]):
                print("_", end="")
            for y in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """Print instance"""
        square_str = ""

        if self.__size > 0:
            for x in range(self.__position[1]):
                square_str += "\n"
            for y in range(self.__size):
                square_str += " " * self.__position[0]
                square_str += "#" * self.__size + "\n"
        return square_str[:-1]
