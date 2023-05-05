#!/usr/bin/python3
"""Takes github credentials and used the github api to display id"""
from requests.auth import HTTPBasicAuth
import requests as rq
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    res = rq.get(url, auth=HTTPBasicAuth(username, password))
    try:
        obj = res.json()
        print(obj.get('id'))
    except ValueError:
        print(None)
