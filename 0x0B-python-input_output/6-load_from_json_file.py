#!/usr/bin/python3
"""Create Object module"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

        Args:
            filename: file to write to
    """
    with open(filename, encoding="utf-8") as file_obj:
        return json.load(file_obj)
