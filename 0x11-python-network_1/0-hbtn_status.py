#!/usr/bin/python3
"""
Python script that fetches an internet resources
"""
import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        response = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response.decode("utf8")))
