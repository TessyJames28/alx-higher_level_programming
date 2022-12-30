#!/usr/bin/python3
"""module that write the first and last name"""


def say_my_name(first_name, last_name=""):
    """
    function that prints first and last name as argument

    Arguments:
        first_name (string): `first_name` mandatory
        last_name (string): `last_name` optional

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string

    Return:
        Nothing
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
