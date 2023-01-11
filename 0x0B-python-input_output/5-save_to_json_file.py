#!/usr/bin/python3
"""function that writes json object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
