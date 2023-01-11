#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    read file text via UTF8 encoding

    Arguments
        filename - variable that holds the text path
    """

    with open(filename, encoding="UTF8") as file:
        print(file.read(), end="")
