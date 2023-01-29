#!/usr/bin/python3
""" the print_square module """


def print_square(size):
    """ prints a square based on size """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if size == 0:
        print()
    for row in range(size):
        for col in range(size):
            print("#", end='')
        print()
