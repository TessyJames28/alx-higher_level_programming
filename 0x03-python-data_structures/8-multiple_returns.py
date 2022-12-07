#!/usr/bin/python3


def multiple_returns(sentence):
    """
    function that returns a tuple with the length of a string
    and its first character
    """
    if sentence != "":
        multiple_returns = (len(sentence), sentence[0])
    else:
        multiple_returns = (len(sentence), 'None')
    return multiple_returns
