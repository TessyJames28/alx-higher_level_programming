#!/usr/bin/python3
"""a class Student"""


class Student:
    """A class student with public instance fisrt_name, last_name, age"""
    def __init__(self, first_name, last_name, age):
        """
        Arguments:
            first_name - string
            last_name - string
            age - int
        Returns:
            retirves a dictionary representation of a Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
