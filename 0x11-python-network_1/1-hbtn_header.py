#!/usr/bin/python3
"""A python script that takes a URL"""
from urllib import request as rq
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        with rq.urlopen(sys.argv[1]) as response:
            print(response.headers['X-Request-Id'])
