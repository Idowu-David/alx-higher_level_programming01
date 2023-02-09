#!/usr/bin/python3
""" defines a Student class """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        """ instance initializer """
        if type(first_name) is not str:
            raise ValueError("first_name must be a string")
        self.first_name = first_name
        if type(last_name) is not str:
            raise ValueError("last_name must be a string")
        self.last_name = last_name
        if age < 0:
            raise ValueError("age cannot be less than 0")
        self.age = age

    def to_json(self):
        """ retrives a dictionary representation of Student object """
        return self.__dict__
