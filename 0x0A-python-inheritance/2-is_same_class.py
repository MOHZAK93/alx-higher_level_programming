#!/usr/bin/python3

"""isinstance module"""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of specified class
        Otherwise False

        Args:
            obj: object to check
            a_class: class to compare
    """
    if isinstance(obj, a_class):
        return True
    return False
