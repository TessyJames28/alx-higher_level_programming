#!/usr/bin/python3
"""function that write string to a textfile (UTF8)"""


def write_file(filename="", text=""):
    """write and print the total size of content written"""
    with open(filename, "w", encoding="UTF8") as file:
        return file.write(text)
