#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    ssum = avg = 0
    mult = 1
    for tup in my_list:
        mult = tup[0] * tup[1]
        avg += tup[1]
        ssum += mult
    return ssum / avg
