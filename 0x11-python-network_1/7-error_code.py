#!/usr/bin/python3
"""Error code #1"""
import requests as rq
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = rq.get(url)
    if res.status_code < 400:
        print(res.text)
    else:
        print(f"Error code: {res.status_code}")
