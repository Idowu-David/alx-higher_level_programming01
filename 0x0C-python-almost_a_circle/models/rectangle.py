#!/usr/bin/python3
""" Rectangle class module """
from models.base import Base


class Rectangle(Base):
    """ defines a Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = id
