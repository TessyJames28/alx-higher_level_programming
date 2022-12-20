#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Write a function that prints an integer.
    value can be any type (integer, string, etc.)
    The integer should be printed followed by a new line
    Returns True if value has been correctly printed
    (it means the value is an integer)
    Otherwise, returns False and prints in stderr the error precede by
    Exception
    """
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    return True
