#!/usr/bin/python3
"""function that search and update file based on a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing
    a specific string

    Arguments:
        filename - name of text file
        search_string - string to search for
        new_string - string to be replaced with
    """

    string = ""
    with open(filename) as f:
        for lines in f:
            string += lines
            if search_string in lines:
                string += new_string
    with open(filename, "w", encoding="utf-8") as text:
        text.write(string)
