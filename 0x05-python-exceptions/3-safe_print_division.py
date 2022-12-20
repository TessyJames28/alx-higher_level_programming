#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Write a function that divides 2 integers and prints the result.
    You can assume that a and b are integers
    The result of the division should print on the finally: section
    preceded by Inside result:
    Returns the value of the division, otherwise: None
    """
    res = None
    try:
        res = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(res))

    return res
