#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays
the value of the variable X-Request-Id
in the response header
"""
import requests
import sys

if __name__ == '__main__':
    try:
        resp = requests.get(sys.argv[1])
        print(resp.header['X-Request-Id'])
    except:
        pass
