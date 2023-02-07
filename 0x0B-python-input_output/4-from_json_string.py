#!/usr/bin/python3
"""JSON module"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented
        by a JSON string

        Args:
            my_str: string to convert to object
    """
    return json.loads(my_str)
