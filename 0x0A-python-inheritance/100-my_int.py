#!/usr/bin/python3
"""a class MyInt that inherits int"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, value):
        """override == operator with != operator"""
        return self.real != value

    def __ne__(self, value):
        """override != operator with == operator"""
        return self.real == value
