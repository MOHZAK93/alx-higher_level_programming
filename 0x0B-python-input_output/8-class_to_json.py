#!/usr/bin/python3
"""Class to JSON module"""
import json


def class_to_json(obj):
    """Returns dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object

        Args:
            obj: instance of a class
    """
    return json.load(obj)
