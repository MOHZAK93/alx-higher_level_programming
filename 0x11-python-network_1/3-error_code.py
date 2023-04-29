#!/usr/bin/python3
"""Displays the body of the response"""
from urllib import request as rq, error
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            with rq.urlopen(url) as response:
                print(response.read().decode('utf-8'))
        except error.HTTPError as ex:
            print('Error code: {}'.format(ex.code))
