#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """Defines BaseGeometry class"""

    def area(self):
        """Calculates area of geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Args:
            name: first argument
            value: second argument
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
