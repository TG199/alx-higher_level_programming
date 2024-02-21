#!/usr/bin/python3
"""Json file
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


file_name = "add_item.json"
obj = []

if os.path.exists(file_name):
    obj = load_from_json_file(file_name)

for arg in sys.argv[1:]:
    obj.append(arg)
save_to_json_file(obj, file_name)
