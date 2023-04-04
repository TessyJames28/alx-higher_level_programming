#!/usr/bin/python3
"""
Python script that sends a request to the URL and displays the value
    display value of the variable X-Request-Id in the response header
    You must use the packages requests and sys
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    value = r.headers.get('X-Request-Id')
    print(value)
