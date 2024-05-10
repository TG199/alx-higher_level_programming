#!/usr/bin/python3
"""
X-Request-Id
"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as resp:
        req_id = resp.headers.get('X-Request-Id')
        print(req_id)
