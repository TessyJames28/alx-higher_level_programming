#!/usr/bin/python3
"""module prints a text with 2 new lines after these characters: ., ? and :"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Argument:
        text (str): `text` must be a string

    Raises:
        TypeError: text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while (i < len(text) and i == " "):
        i += 1
    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in "?.:":
            if text[i] in "?.:":
                print("\n")
            i += 1

            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
