#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """
    class:
        `Mylist`
    inherits:
        `list`
    """

    def print_sorted(self):
        """
        a public instance method that sort
        and print the list in ascending order
        """
        print(sorted(self))
