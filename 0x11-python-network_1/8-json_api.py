#!/usr/bin/python3
"""
A python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
    The letter must be sent in the variable q
    If no argument is given, set q=""
    If the response body is properly JSON formatted and not empty,
    display the id and name like this: [<id>] <name>
    Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
    You must use the package requests and sys
"""
import requests
import sys


if __name__ == "__main__":
    q = ""
    if len(sys.argv) > 1 and sys.argv[1].isalpha() is not False:
        q = sys.argv[1]
    data = {"q": q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        if (r.json() and len(r.json()) > 0):
            value = r.json()
            id = value.get("id")
            name = value.get("name")
            print("[{}] {}".format(id, name))
        elif len(r.json()) == 0:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
