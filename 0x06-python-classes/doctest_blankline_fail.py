#doctest_blankline_fail.py

def double_space(lines):
    """Prints a list of lines double-space.

    >>> double_space(['Line one.', 'Line two.'])
    Line one.
    <BLANKLINE>
    Line two.
    <BLANKLINE>
    """
    for l in lines:
        print(l)
        print()
