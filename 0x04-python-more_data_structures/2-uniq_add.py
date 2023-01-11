#!/usr/bin/python3

def uniq_add(my_list=[]):
    if not my_list:
        return
    uniq = []
    for idx in range(len(my_list)):
        if my_list[idx] not in uniq:
            uniq.append(my_list[idx])
    ssum = 0
    for ele in uniq:
        ssum += ele
    return ssum
