#!/usr/bin/python3
"""module for print_square"""


def print_square(size):
    """
    function that prints square

    Argument:
        size (int): `size` is mandatory and should be int
                    size can be float if not less than 0

    Raises:
        TypeError: `size` must be an integer
        ValueError: `size` must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")


if __name__ == "__main__":
    doctest.testfile("./tests/4-print_square.txt")
