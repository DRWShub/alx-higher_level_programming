#!/usr/bin/python3
"""Script fetches a URL, and gets a response"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv
from urllib.parse import urlencode


def display_error(url_str: str):
    try:
        req = Request(url_str)
        with urlopen(req) as response:
            output_body = response.read()
        print(output_body.decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    try:
        display_error(argv[1])
    except IndexError:
        raise
