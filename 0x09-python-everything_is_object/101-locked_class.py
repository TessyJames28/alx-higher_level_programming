#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    A class with no class or object attributes that prevents user from
    dynamically creating new instance attribute except "First_name".
    """

    __slots__ = ["first_name"]
