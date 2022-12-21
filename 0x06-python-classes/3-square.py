#!/usr/bin/python3
"""a class Square with private instance attribute size"""


class Square:
    """initializing the class attribute size"""
    def __init__(self, size=0):
        """instantiating the class attribute size

        Args:
            size (int): the size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """defining a public instance area to return area of a square"""
    def area(self):
        return self.__size**2
