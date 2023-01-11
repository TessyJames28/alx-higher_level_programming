#!/usr/bin/python3
"""function that appends a string to text file (UTF8)"""


def append_write(filename="", text=""):
    """appends text and returns the number of words appended"""
    with open(filename, "a", encoding="UTF8") as file:
        return file.write(text)
