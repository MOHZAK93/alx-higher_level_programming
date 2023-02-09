#!/usr/bin/python3
"""Add attribute module"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it is possible"""
    try:
        obj.name = value
    except Exception:
        raise TypeError("can't add new attribute")
