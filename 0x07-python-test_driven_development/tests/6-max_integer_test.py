#!/usr/bin/python3
"""unittest module for max_integer"""
import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test class for max_integer

    Arguments:
        inherits from unittest
    """

    def test_module_docstring(self):
        """test module for doctring"""
        m = ("6-max_integer").__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """test function for docstring"""
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_max_integer(self):
        """check for ordered list"""
        res = max_integer([1, 2, 3, 5, 6, 7])
        self.assertEqual(7, res)

    def test_multiple_max_integer(self):
        """check for multiple max integer value"""
        res = max_integer([1, 7, 3, 7, 6, 7])
        self.assertEqual(7, res)

    def test_unordered_list(self):
        """check for unorederd list"""
        res = max_integer([7, 4, 2, 1, 10, 8])
        self.assertEqual(10, res)

    def test_empty_list(self):
        """correct test for empty list"""
        res = max_integer([])
        self.assertEqual(None, res)

    def test_tuple(self):
        """test for tuple and raises type error"""
        self.assertRaises(TypeError, max_integer, (6, "a", 1, 2))

    def test_string(self):
        """test for string"""
        res = max_integer(["Master"])
        self.assertTrue("t", res)

    def test_list_of_string(self):
        """test for list of string"""
        res = max_integer(["My", "name", "is", "tessy"])
        self.assertEqual("tessy", res)

    def test_float(self):
        """test for float"""
        res = max_integer([15.1, 2.4, 0.33, 20.7, 1.80])
        self.assertTrue(20.7, res)


if __name__ == "__main__":
    unittest.main()
