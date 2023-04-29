#!/usr/bin/python3
"""A python script that fetches a URL"""
import requests as rq


if __name__ == "__main__":
    res = rq.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
