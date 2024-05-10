#!/usr/bin/python3
""" A script to fetch a particular URL
"""
import urllib

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as resp:
    if resp.statuscode == 200:
        body = resp.content
        type_ = type(body)
        utf_8 = body.decode('utf-8')

        print("Body response:")
        print("  - type: {type_}")
        print("  - content: {body}")
        print("  - utf8 content: {utf_8")
