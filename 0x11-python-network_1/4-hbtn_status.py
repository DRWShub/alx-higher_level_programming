#!/usr/bin/python3
"""Script fetches a URL, and gets a response"""
import requests


def make_request():
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))


if __name__ == "__main__":
    make_request()
