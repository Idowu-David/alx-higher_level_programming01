#!/usr/bin/python3
""" The add_integer module """


def add_integer(a, b=98):
    """ add_integer: adds two given integers

        Args:
            a(int): first integer
            b(int): second integer
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int or a + 1 == a:
        raise TypeError("a must be an integer")
    if type(b) is not int or b + 1 == b:
        raise TypeError("b must be an integer")
    return a + b
