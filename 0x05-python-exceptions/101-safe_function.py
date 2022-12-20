#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Write a function that executes a function safely.
    You can assume fct will be always a pointer to a function
    Returns the result of the function,
    Otherwise, returns None if something happens during the function
    and prints in stderr the error precede by Exception:
    """
    res = None
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
    return res
