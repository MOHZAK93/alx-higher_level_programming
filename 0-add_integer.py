#!/usr/bin/python3
"""Add integer module
"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a (int | float): First integer.
        b (:obj:`int|float`, optional): Second integer. Defaults to 98.

    Returns:
        The sum of the two integers.
    Raises:
        TypeError: If `a` or `b` is not of type int or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
