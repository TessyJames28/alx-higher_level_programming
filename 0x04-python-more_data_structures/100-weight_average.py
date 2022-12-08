#!/usr/bin/python3


def weight_average(my_list=[]):
    """
    function that returns the weighted average of all integers
    tuple (<score>, <weight>)
    """
    if not my_list:
        return 0
    sums = 0
    w_sums = 0
    for idx in my_list:
        sums += idx[0] * idx[1]
        w_sums += idx[1]
    return sums / w_sums
