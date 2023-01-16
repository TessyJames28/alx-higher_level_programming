#!/usr/bin/python3
"""Defines class Rectangle that inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle with private instance attributes with getters/setters

    Attributes:
        width (int) - width of the rectangle
        height (int) - height of the rectangle
        x (int) - must be >= 0
        y (int) - must be >= 0
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
        Base.id = id

    @property
    def width(self):
        """get/set width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get/set height of a Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get/set x property of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get/set y property of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of a rectangle"""
        return self.height * self.width

    def display(self):
        """displays the Rectangle values as "#" character"""
        if self.width == 0 or self.height == 0:
            return ""

        [print(" ") for y in range(self.y)]
        for w in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for h in range(self.width)]
            print()

    def __str__(self):
        """prints a specific format for rectangle string representation"""
        new_str = "[" + str(__class__.__name__) + "]" + " " + "("
        new_str += str(self.id) + ")" + " " + str(self.x) + "/" + str(self.y)
        new_str += " - " + str(self.width) + "/" + str(self.height)
        return new_str

    def update(self, *args, **kwargs):
        """assigns arguments to each of the Rectangle instance attributes

        Arguments:
            *args - contains a variable number of no-keyword argument
            attr - argument within the attrs
            elem - counts the number of elements/arguments
            **kwargs -  assigns a key/value argument to attributes

            Arguments:
                args0 - self.id
                args1 - self.width
                args2 - self.height
                args3 - self.x
                args4 - self.y

        """

        if args and len(args) != 0:
            elem = 0
            for attr in args:
                if elem == 0:
                    if attr is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = attr
                elif elem == 1:
                    self.width = attr
                elif elem == 2:
                    self.height = attr
                elif elem == 3:
                    self.x = attr
                elif elem == 4:
                    self.y = attr

                elem += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value == "None":
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y

            }
