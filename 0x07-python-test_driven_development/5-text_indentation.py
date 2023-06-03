#!/usr/bin/python3
"""Text Indentation module"""


def text_indentation(text):
    """Prints text with 2 new lines after each of these characters
    ., ? and :

    Args:
        text: text to print

    Raises:
        TypeError: text must be a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < (len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print()
            i += 2
            continue
        print(text[i], end="")
        i += 1
