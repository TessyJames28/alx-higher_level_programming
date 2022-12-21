#!/usr/bin/python3
"""a class Square with private instance attribute size"""


class Square:
    """initializing the class attribute size"""
    def __init__(self, size=0):
        self.__size = size
        """instantiating the class attribute size

        Args:
            size (int): the size of the new square
        """
    """defining @property to get size value"""
    @property
    def size(self):
        return self.__size

    """defining the setter to set the size value"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """defining a public instance method "area" to return area of a square"""
    def area(self):
        return self.__size**2

    """defining a public instance method "my_print" to print to stdout"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
