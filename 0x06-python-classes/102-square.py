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
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """defining a public instance method "area" to return area of a square"""
    def area(self):
        return self.__size**2

    """defining comparisons for Square instance using python magic operators"""
    def __eq__(self, val):
        return self.area() == val.area()

    def __ne__(self, val):
        return self.area() != val.area()

    def __lt__(self, val):
        return self.area() < val.area()

    def __ge__(self, val):
        return self.area() >= val.area()

    def __gt__(self, val):
        return self.area() > val.area()

    def __le__(self, val):
        return self.area() <= val.area()
