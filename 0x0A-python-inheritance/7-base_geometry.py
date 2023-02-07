#!/usr/bin/python3

"""BaseGeometry module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer

        Args:
            name: first argument
            value: second argument
        """
        self.name = name
        self.value = value
        if type(self.value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
