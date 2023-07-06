#!/usr/bin/python3
"""This fetches https://intranet.hbtn.io/status."""
import requests


def make_request():
    req = requests.get("http://0.0.0.0:5000/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))


if __name__ == "__main__":
    make_request()
