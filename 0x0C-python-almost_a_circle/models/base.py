#!/usr/bin/python3
""" Base model module """


class Base:
    __nb_object = 0
    def __init__(self, id=None):
        """ instance initialiser """
        if id:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
