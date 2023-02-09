#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """Inherits from int"""
    def __eq__(self, num):
        """When == is called return !="""
        return super().__ne__(num)

    def __ne__(self, num):
        """When != is called return =="""
        return super().__eq__(num)
