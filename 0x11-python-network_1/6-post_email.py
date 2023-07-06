#!/usr/bin/python3
"""The script sends POST request"""
import requests
from sys import argv


def display_request(url: str, email_arg: str):
    payload = {"email": email_arg}
    req = requests.post(url, data=payload)
    print(req.text)


if __name__ == "__main__":
    display_request(argv[1], argv[2])
