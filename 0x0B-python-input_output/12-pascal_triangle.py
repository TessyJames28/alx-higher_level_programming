#!/usr/bin/python3
"""Technical interview preparation"""


def pascal_triangle(n):
    """
    function that creates a pascal triangle

    Arguments:
        n - number of triagles to be created
    Returns:
        an empty list if n <= 0
        a list of lists of integers representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    n_pascal = [[1]]
    while len(n_pascal) != n:
        n_tri = n_pascal[-1]
        n_temp = [1]

        for idx in range(len(n_tri) - 1):
            n_temp.append(n_tri[idx] + n_tri[idx + 1])
        n_temp.append(1)
        n_pascal.append(n_temp)
    return n_pascal
