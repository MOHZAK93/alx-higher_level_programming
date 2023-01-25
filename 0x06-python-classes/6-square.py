#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a size.

        Args:
            size: size of square
            position: position of square
        """
        self.__size = size
        self.__position = position

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
        for x in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """Method to retrieve position

        Returns:
            coordinates of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Method to set the position

        Args:
            value: value of position
        """
        if (
                not isinstance(value, tuple)
                or len(value) != 2
                or type(value[0]) != int
                or type(value[1]) != int
                or value[0] < 0
                or value[1] < 0
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
