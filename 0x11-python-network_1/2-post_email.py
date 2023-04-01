#!/usr/bin/python3
"""
Python script that takes a URL and sends a post request
    accepts email as a parameter
    dsiplay the response decoded in utf-8
"""
import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":

    val = {'email': sys.argv[2]}
    value = urllib.parse.urlencode(val).encode('ascii')
    req = urllib.request.Request(sys.argv[1], value)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
