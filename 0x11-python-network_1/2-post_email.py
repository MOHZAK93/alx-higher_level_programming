#!/usr/bin/python3
"""A python script that takes a URL"""
from urllib import request as rq, parse
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        _data = bytes(parse.urlencode([('email', email)]), 'utf-8')
        with rq.urlopen(url, data=_data) as response:
            print(response.read().decode('utf-8'))
