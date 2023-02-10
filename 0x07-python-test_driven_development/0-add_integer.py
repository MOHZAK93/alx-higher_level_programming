#!/usr/bin/python3
"""Add Integer"""


def add_integer(a, b=98):
    """Adds two integers
    args:
        a (int|float): first integer
        b (:obj:`int|float`, optional): second integer. Defaults to 98
    Returns:
        The sum of the two integers as a whole number
    Raises:
        TypeError: If `a` or `b` is not int or float
    """
    if type(a) not in [int, float] or a in (float('inf'), -float('inf')):
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b in (float('inf'), -float('inf')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
