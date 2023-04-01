#!/usr/bin/python3
"""
Python script that takes a URL and sends a request that displays the body
    Manage the urllib.error.HTTPError exceptions
    displays <error code>: <HTTP status code>
"""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
