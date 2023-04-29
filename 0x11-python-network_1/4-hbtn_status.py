#!/usr/bin/python3
"""A python script that fetches a URL"""
from urllib import request as rq


if __name__ == "__main__":
    with rq.urlopen('https://alx-intranet.hbtn.io/status') as response:
        if response.readable():
            html = str(response.read())
            print("Body response:")
            print("\t- type: {}".format(type(html)))
            print("\t- content: {}".format(html))
