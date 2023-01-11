#!/usr/bin/python3
"""a class Student that convert to JSON with filter"""


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

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list

        Args:
            attrs (list): (Optional) The attributes to represent.
        """

        if (type(attrs) == list and
                all(type(items) == str for items in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
