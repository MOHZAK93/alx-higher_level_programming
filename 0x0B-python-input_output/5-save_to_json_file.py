#!/usr/bin/python3
"""Save Object module"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation

        Args:
            my_obj: object to write
            filename: file to write to
    """
    with open(filename, 'w') as f:
        f.write(str(my_obj))
