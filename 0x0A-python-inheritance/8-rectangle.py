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
        self.__width = width
        self.__heigth = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
