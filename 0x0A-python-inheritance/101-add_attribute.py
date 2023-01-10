#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr, value):
    """
    Adds attributes if possible

    Arguments:
        `obj` - the object to add an attribute to
        `attr` (str) - the new attribute to be added
        `value` the value of the attribute
    Raises:
        TypeError: can't add new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
