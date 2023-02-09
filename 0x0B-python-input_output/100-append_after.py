#!/usr/bin/python3
""" append_after module """


def append_after(filename="", search_string="", new_string=""):
    with open(filename) as f:
        text = f.readlines()
    idx = 0
    with open(filename, "w", encoding="utf-8") as f:
        for item in text:
            f.write(item)
            if search_string in item:
                f.write(new_string)
