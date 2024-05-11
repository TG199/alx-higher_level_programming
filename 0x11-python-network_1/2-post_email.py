#!/usr/bin/python3
"""
Make a POST request
"""
from urllib import request, parse
import sys

if __name__ == '__main__':
    email = {'email': sys.argv[2]}
    data = parse.urlencode(email)
    data = data.encode("ascii")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as resp:
        body = resp.read()
        print(body.decode('utf-8'))
