#!/usr/bin/python3

"""Only sub class module"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that
        that inherited from the spcified class; otherwise False

    Args:
        obj: object to check
        a_class: class to compare
    """
    return (type(obj) != a_class)
