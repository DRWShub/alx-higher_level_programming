#!/usr/bin/python3
"""This fetches https://intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    r = requests.get("http://0.0.0.0:5000/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
