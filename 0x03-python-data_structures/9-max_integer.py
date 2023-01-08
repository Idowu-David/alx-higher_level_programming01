#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    l_max = my_list[0]
    for val in my_list:
        if val > l_max:
            l_max = val
    return l_max
