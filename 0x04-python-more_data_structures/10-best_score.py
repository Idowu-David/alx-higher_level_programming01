#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxx = 0
    for key, value in a_dictionary.items():
        if value > maxx:
            maxx = value
            max_key = key
    return max_key
