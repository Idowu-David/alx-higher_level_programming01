#!/usr/bin/python3
""" append_write module """


def append_write(filename="", text=""):
    """ add texts to a file """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
