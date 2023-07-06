#!/usr/bin/python3
"""Script fetches a URL, and gets a response"""
import requests
from sys import argv


def display_status_error(url: str):
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)


if __name__ == "__main__":
    display_status_error(argv[1])
