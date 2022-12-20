#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Write a function that prints the first x elements of a list and only int
    Prototype: def safe_print_list_integers(my_list=[], x=0):
    my_list can contain any type (integer, string, etc.)
    All integers have to be printed on the same line followed by a new line
    other type of value in the list must be skipped (in silence).
    x represents the number of elements to access in my_list
    x can be bigger than the length of my_list - if it’s the case
    an exception is expected to occur
    Returns the real number of integers printed
    """
    ret = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            ret += 1
        except (ValueError, TypeError, NameError):
            continue
    print()

    return ret
