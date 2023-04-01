#!/usr/bin/python3
"""
Python script that fetches url resources
    you must use package requests
"""


if __name__ == "__main__":
    import requests

    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
