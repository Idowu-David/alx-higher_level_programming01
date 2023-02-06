#!/usr/bin/python3
""" defines the lookup module """


def lookup(obj):
    """ returns the list of available atteibutes and
        methods of an object
        Args:
            obj: object to lookup
    """
    return dir(obj)
