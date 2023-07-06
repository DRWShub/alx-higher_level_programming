#!/usr/bin/python3
"""Script takes GitHub credentials and uses GitHub API"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    with requests.get('https://api.github.com/user', auth=auth) as reqst:
        print(reqst.json().get('id'))
