#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Write a function that prints x elements of a list.
    All elements must be printed on the same line followed by a new line.
    x represents the number of elements to print
    x can be bigger than the length of my_list
    Returns the real number of elements printed
    """
    ret = 0
    try:
        for idx in range(x):
            print(my_list[idx], end="")
            ret += 1
    except IndexError as error:
        print()

    if ret == x:
        print()
    return (ret)
