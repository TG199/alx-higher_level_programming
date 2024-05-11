#!/usr/bin/python3
"""
Write a Python script that fetches
https://alx-intranet.hbtn.io/status
"""

import requests

if __name__ == '__main__':

    url = requests.get('https://alx-intranet.hbtn.io/status')

    type_ = url.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type_), type_)
