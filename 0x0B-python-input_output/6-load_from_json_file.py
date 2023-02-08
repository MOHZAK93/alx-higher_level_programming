#!/usr/bin/python3
"""Create Object module"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

        Args:
            filename: file to write to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.loads(f)
