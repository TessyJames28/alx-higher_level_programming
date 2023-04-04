#!/usr/bin/python3
"""
Python script that sends a request to display the body of the response
    If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value of the HTTP status code
    You must use the packages requests and sys
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code:", r.status_code)
    else:
        print(r.text)
