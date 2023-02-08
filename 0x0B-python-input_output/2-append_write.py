#!/usr/bin/python3
"""Append module"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and
        returns the number of characters added

        Args:
            filename: name of file to append to
            text: string to append

        Returns:
            number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as file_obj:
        return file_obj.write(text)
