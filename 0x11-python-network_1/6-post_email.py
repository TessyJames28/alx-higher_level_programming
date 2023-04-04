#!/usr/bin/python3
"""
Python script that sends a a post request with email as parameter
    The email must be sent in the variable email
    You must use the packages requests and sys
"""
import requests
import sys


if __name__ == "__main__":
    post_value = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=post_value)
    print(r.text)
