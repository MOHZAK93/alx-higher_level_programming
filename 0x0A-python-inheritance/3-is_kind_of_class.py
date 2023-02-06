#!/usr/bin/python3

"""Same class or inherit module"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of or if the object
    is an instance of a class that from that spcified class
    otherwise False

    Args:
        obj: object to check
        a_class: class to compare
    """
    return (isinstance(obj, a_class))
