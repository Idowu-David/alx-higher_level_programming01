#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    div_2 = []
    for val in my_list:
        if val % 2 == 0:
            div_2.append(True)
        else:
            div_2.append(False)
    return div_2
