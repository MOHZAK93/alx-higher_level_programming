#!/usr/bin/python3
"""Save Object module"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation

        Args:
            my_obj: object to write
            filename: file to write to
    """
    with open(filename, 'w', encoding="utf-8") as file_obj:
        json.dump(my_obj, file_obj)
