#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """
    Name:
        BaseGeometry

    Methods:
        area()
        integer_validator() (objects):
            name: always a string
            value (int)

    Raises:
        Exception: area() is not implemented
        TypeError: <name> must be an integer
        TypeError: <name> must be greater than 0
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(self.value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
