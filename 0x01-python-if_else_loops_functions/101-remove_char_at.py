#!/usr/bin/python3

def remove_char_at(str, n):
    cpy = ""
    for i in range(len(str)):
        if i != n:
            cpy = cpy + str[i]
    return cpy
