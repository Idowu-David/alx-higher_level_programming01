#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    keys = []
    for key in a_dictionary.keys():
        keys.append(key)
    keys = sorted(keys)
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
