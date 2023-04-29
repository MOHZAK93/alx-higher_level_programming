#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter"""
import requests as rq, parse
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        _data = [('email', email)]
        res = rq.post(url, data_data)
        print(res.text)
