#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if not a_dictionary:
        return
    new_dict = a_dictionary.copy()
    for ele in new_dict.keys():
        if ele == key:
            a_dictionary[key] = value
    if key not in new_dict.keys():
        a_dictionary[key] = value
    return a_dictionary
