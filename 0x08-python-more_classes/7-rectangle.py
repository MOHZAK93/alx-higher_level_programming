#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Defines a rectangle"""

    """A public class attribute counting the number of rectangles"""
    number_of_instances = 0

    """A public class attribute used as a symbol for string representation"""
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes rectangle object
        Args:
            width: width of rectangle
            height: height of rectangle
        """

        self.width = width
        self.height = height

        """Increases number of rectangles by 1"""
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """String representation of rectangle using #
        """
        return ((str(self.print_symbol) * self.__width + "\n")
                * self.__height).rstrip()

    def __repr__(self):
        """String representation of rectangle to recreate a new instance
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Called when an instance is deleted
        """
        print("Bye rectangle...")

        """Decreases number of rectangles by 1"""
        Rectangle.number_of_instances -= 1
