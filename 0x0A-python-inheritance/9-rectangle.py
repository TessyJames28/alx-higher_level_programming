#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    instantiation:
        width (private) - no getter or setter
        height (private) - no getter or setter

    Value:
        width and height must be positive integer
        validated by integer_validator
    """

    def __init__(self, width, height):
        BaseGeometry.__init__(self)

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """
        print() should print, and str() should return, the following
        rectangle description: [Rectangle] <width>/<height>
        """
        print_string = "[" + self.__class__.__name__ + "] "
        print_string += str(self.__width) + "/" + str(self.__height)

        return print_string
