#!/usr/bin/python3
"""a class called Square"""


class Square:
    """initializing class as a private instance"""
    def __init__(self, size=0):
        self.__size = size
        """instantiating private instance attribute size

        Args:
            size (int): the size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
