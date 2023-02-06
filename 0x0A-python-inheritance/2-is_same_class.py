#!/usr/bin/python3
""" is_same_class module """


def is_same_class(obj, a_class):
    """ returns True if the obj is exactly the same class of a_class
    otherwise False

    Args:
        obj: object
        a_class: class to be checked
    """
    return type(obj) is a_class
