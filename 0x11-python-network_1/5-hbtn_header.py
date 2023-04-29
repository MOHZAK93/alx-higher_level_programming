#!/usr/bin/python3
"""Displays the value of th variable X-Request-Id"""
import requests as rq
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = rq.get(sys.argv[1])
        if 'X-Request-Id' in res.headers:
            print(res.headers['X-Request-Id'])
