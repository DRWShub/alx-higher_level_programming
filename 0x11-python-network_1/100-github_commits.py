#!/usr/bin/python3
"""Lists 10 commits from recent to oldest in  a repository"""
import requests
import sys


if __name__ == '__main__':
    URL = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    with requests.get(URL) as response:
        reqst = response.json()
        try:
            for i in range(0, 10):
                name = reqst[i].get('sha')
                sha = reqst[i].get('commit').get('author').get('name')
                print('{}: {}'.format(name, sha))
        except Exception:
            pass
