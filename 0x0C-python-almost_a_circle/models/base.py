#!/usr/bin/python3
""" Base model module """
import json


class Base:
    __nb_object = 0
    def __init__(self, id=None):
        """ instance initialiser """
        if id:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries:

        list_dictionaries is a list of dictionaries
        If list_dictionaries is None or empty, return the string: "[]"

        Otherwise, return the JSON string representation of list_dictionaries
        """
        if not list_dictionaries or list_dictionaries == None:
            return "[]"
        json_dict = []
        return json.dumps(list_dictionaries)
