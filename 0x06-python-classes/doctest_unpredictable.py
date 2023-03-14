#doctest_unpredictable.py

class MyClass:
    pass


def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<doctest_unpredictable.MyClass object at 0x...>]
    """
    return [obj]
