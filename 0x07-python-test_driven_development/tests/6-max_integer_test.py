#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_int(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([5, 6, 7]), 7)
        self.assertEqual(max_integer([2, 8, 6]), 8)
        self.assertEqual(max_integer([7, 3, 6]), 7)
        self.assertEqual(max_integer([-10, -3, -4]), -3)
        self.assertEqual(max_integer([-2]), -2)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([1, 5, 8]), 8)
        self.assertEqual(max_integer([11, 8, 7]), 11)

    def test_empty(self):
        self.assertIsNone(max_integer([]))


if __name__ == "__main__":
    unittest.main()
