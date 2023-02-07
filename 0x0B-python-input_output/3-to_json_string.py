#!/usr/bin/python3
import json
"""JSON module"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string)

        Args:
            my_obj: object
    """
    return json.dumps(my_obj)
