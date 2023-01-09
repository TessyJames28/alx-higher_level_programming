#!/usr/bin/python3
"""function that checks for object instance"""


def is_same_class(obj, a_class):
    """
    Arguments:
            obj (any) - the object to check
            a_class (type) - class to matcht the object
    Returns:
        `True` - if the object is exactly an instance of the specified class
        `False` - if otherwise
    """

    if type(obj) is a_class:
        return True
    return False
