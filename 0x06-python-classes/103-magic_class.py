#!/usr/bin/python3
"""Defines a Magiclass based by interpreting bytecode provided by ALX"""


import math


class MagicClass:
    """represents a circle"""

    def __init__(self, radius=0):
        """initializing a MagicClass"""
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        return (2 * math.pi * self.__radius)
