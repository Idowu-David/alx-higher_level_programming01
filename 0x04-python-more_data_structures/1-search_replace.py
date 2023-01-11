#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if not my_list:
        return
    new = my_list[:]
    for idx in range(len(new)):
        if new[idx] == search:
            new[idx] = replace
    return new
