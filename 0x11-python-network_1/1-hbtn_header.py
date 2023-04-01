#!/usr/bin/python3
"""
Python script that fetches an internet resources
    accepts url on the command line
    dsiplay the variable x-Request-Id
"""
import urllib.request
import sys


if __name__ == "__main__":

    req = urllib.request.Request("{}".format(sys.argv[1]))
    with urllib.request.urlopen(req) as response:
        print(response.headers.get("x-Request-Id"))
