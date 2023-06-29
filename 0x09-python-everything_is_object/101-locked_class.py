#!/usr/bin/python3
"""Class LockedClass with no class or object attribute"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance
    Except if the new instance attribute is called first_name
    """
    __slots__ = ["first_name"]
