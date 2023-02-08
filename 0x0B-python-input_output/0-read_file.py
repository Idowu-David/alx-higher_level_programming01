#!/usr/bin/python3
""" read_file module """


def read_file(filename=""):
    """ reads a text and prints it to stdout """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
