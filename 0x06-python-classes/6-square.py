#!/usr/bin/python3
"""a class Square with private instance attribute size"""


class Square:
    """initializing the class attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
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

    """defining @property to get the value of class method position"""
    @property
    def position(self):
        return self.__position

    """definint the setter to set the value of position"""
    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) or
                value != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    """defining a public instance method "area" to return area of a square"""
    def area(self):
        return self.__size**2

    """defining a public instance method "my_print" to print to stdout"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                if j == 0:
                    print(" " * self.__position[0], end="")
                print("#", end="")
            print()
