#!/usr/bin/python3
def magic_string():
    magic_string.val = getattr(magic_string, 'val', 0) + 1
    return ("BestSchool, " * (magic_string.val - 1) + "BestSchool")
