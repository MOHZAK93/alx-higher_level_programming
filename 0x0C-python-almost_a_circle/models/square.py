#!/usr/bin/python3
"""First Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square

        Args:
            Rectangle: parent class to square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square

        Args:
                size: size of square
                x: horizontal offset
                y: vertical offset
                id: id of square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size of square"""

        return self.width

    @size.setter
    def size(self, value):
        """Setter for size of square"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates square object arguments

        Args:
                args: non-keyword argument
                kwargs: keyword argument
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

        if args is not None:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]

    def __str__(self):
        """String representation of Square"""

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Dictionary representation of Square"""

        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
