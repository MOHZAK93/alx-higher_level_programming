#!/usr/bin/python3

"""Inheritance module"""


class MyList(list):
    """Inherits from class list"""

    def print_sorted(self):
        """prints sorted list in ascending order"""
        print(sorted(self))
        
