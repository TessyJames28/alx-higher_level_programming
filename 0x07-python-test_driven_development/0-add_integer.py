#!/usr/bin/python3
"""this module adds two integers a and b"""


def add_integer(a, b=98):
    """
    function that adds two integers a and b and returns result

    Arguments:
        a (int): `a`
        b (optional, int): `b`

    Raises:
        TypeError: a must be an int
        TypeError: b must be an int

    Returns:
        int: `a` + `b`
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b


if __name__ == "__main__":
    doctest.testfile("./tests/0-add_integer.txt")
