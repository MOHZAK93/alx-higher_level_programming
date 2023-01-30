#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes rectangle object
        Args:
            width: width of rectangle
            height: height of rectangle
        """

        self.width = width
        self.height = height

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
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves height of rectangle
        """

        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets height of rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
