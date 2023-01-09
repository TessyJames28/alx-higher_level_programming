#!/usr/bin/python3
"""checks for subclass"""


def inherits_from(obj, a_class):
    """
    checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Arguments:
        obj (subclass): object to check
        a_class (superclass): class inherited from

    Returns:
        True: if its a subclass
        False: if otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
