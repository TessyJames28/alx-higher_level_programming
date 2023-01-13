#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance area that returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """public instance that returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns the printable representation of rectangle as'#'"""
        if self.__width == 0 or self.__height == 0:
            return ""

        new_str = []
        for h in range(self.__height):
            [new_str.append("#") for w in range(self.__width)]
            if h != self.__height - 1:
                new_str.append("\n")
        return ("".join(new_str))

    def __repr__(self):
        """return a string representation of rectangle"""
        new_str = "Rectangle(" + str(self.__width)
        new_str += ", " + str(self.__height) + ")"
        return new_str
