#!/usr/bin/python3
"""Print Name module"""


def say_my_name(first_name, last_name=""):
    """Prints first_name and last_name

    Args:
        first_name: first parameter
        last_name: second parameter

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
