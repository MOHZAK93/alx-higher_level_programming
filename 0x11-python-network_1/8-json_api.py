#!/usr/bin/python3
"""Search API"""
import requests as rq
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = {'q': sys.argv[1]}
    else:
        q = {'q': ''}
    res = rq.post(url, data=q)
    try:
        obj = res.json()
        if len(obj) == 0:
            print(f"No result")
        else:
            print(f"[{obj['id']}] {obj['name']}")
    except ValueError:
        print(f"Not a valid JSON")
