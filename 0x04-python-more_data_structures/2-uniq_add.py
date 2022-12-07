#!/usr/bin/python3


def uniq_add(my_list=[]):
    """
    function that adds all unique integers in a list
    (only once for each integer)
    """
    sums = 0
    new_list = set(my_list)
    for i in new_list:
        sums += i

    return sums
