#doctest_private_tests.py

import doctest_private_external

__test__ = {
        'numbers': """
>>> my_function(2, 3)
6

>>> my_function(2.0, 3)
6.0
""",
    
    'strings': """
>>> my_function('a', 3)
'aaa'

>>> my_function(3, 'a')
'aaa'
""",

    'external': doctest_private_external,
}

def my_function(a, b):
    """Returns a * b
    """
    return a * b
