#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    idx = 0
    for val in my_list:
        try:
            if idx != x:
                print("{}".format(my_list[idx]), end="")
                idx += 1
        except IndexError:
            break
    print()
    return idx

