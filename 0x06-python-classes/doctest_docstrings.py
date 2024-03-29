#doctest_docstrings.py

"""Tests can appear in any docstring within the module.
MOdule-level tests cross class and function boundaries.
>>> A('a') == B('b')
False
"""


class A:
    """Simple class.

    >>> A('instance_name').name
    'instance_name'
    """

    def __init__(self, name):
        self.name = name

    def method(self):
        """Returns an unusual value.
        
        >>> A('name').method()
        'eman'
        """
        return ''.join(reversed(self.name))

class B(A):
    """Another simple class.

    >>> B('different_name').name
    'different_name'
    """
