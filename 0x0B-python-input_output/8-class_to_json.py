#!/usr/bin/python3
"""Class to JSON module"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object

        Args:
            obj: instance of a class
    """
    if "__dict__" in dir(obj):
        return obj.__dict__.copy()
    return {}
