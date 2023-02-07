#!/usr/bin/python3

"""Read file module"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout

        Args:
            filename: name of rile to read
    """
    with open(filename, encoding="utf-8") as f:
        f = f.read()
        for line in f:
            print(line, end='')
