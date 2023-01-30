#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, heigth=0):
        """Initializes rectangle object
        Args:
            width: width of rectangle
            heigth: heigth of rectangle
        """

        self.__width = width
        self.__heigth = heigth

    @property
    def width(self):
        """Retrieves width of rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets width of rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def heigth(self):
        """Retrieves heigth of rectangle
        """
        return (self.__heigth)

    @heigth.setter
    def heigth(self, value):
        """Sets heigth of rectangle
        """
        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__heigth = value
