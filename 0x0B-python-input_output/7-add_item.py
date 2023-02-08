#!/usr/bin/python3
""" add_item module 
    adds all arguments to a Python list, and then save them to a file:
"""
import sys
import json


filename = 'add_item.json'
load = __import__("6-load_from_json_file").load_from_json_file
save = __import__("5-save_to_json_file").save_to_json_file

args = sys.argv[1:]

try:
    with open(filename) as f:
        add = load(filename)
    with open(filename, "w") as f:
        for item in args:
            add.append(item)
        f.write(json.dumps(add))
except FileNotFoundError:
    with open(filename, "w") as f:
        add = []
        f.write(json.dumps(add))
