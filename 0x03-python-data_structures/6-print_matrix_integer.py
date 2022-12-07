#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers."""
    for outer_m in matrix:
        for inner_m in outer_m:
            if inner_m == outer_m[-1]:
                print("{:d}".format(inner_m), end="")
            else:
                print("{:d}".format(inner_m), end=" ")
        print("")
