#!/usr/bin/python3

"""Attributes and methods module"""


def lookup(obj):
    """Returns the list of available attributes
        and methods of an object

        Args:
            obj: parameter
        Returns:
            list of object
    """
    return list(obj.__dict__)
