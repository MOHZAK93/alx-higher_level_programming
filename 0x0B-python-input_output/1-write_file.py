#!/usr/bin/python3

"""Write file module"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and
        returns the number of characters written

        Args:
            filename: name of file to write to
            text: string to write

        Returns:
            number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file_obj:
        return file_obj.write(text)
