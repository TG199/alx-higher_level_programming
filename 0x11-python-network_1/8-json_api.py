#!/usr/bin/python3
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys

if __name__ == '__main__':
    data = {'q': ""}

    try:
        data['q'] = sys.argv[1]

    except Exception as e:
        pass

    resp = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_o = resp.json()
        if not json_o:
            print("No result ")
        else:
            print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
    except Exception as e:
        print("Not a valid JSON")
