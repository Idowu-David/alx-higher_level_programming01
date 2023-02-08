#!/usr/bin/python3
""" write_file module """


def write_file(filename="", text=""):
    """ writes a text to a file """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
