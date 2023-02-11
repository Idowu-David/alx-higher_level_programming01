#!/usr/bin/python3
""" Rectangle class module """
from models.base import Base


class Rectangle(Base):
    """ defines a Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        self.setter_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        self.setter_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        self.setter_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        self.setter_validator("y", value)
        self.__y = value

    def area(self):
        """ calculates and returns the area value of Rectangle instance """
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        x, y = self.x, self.y
        print("\n" * y, end="")
        for row in range(self.height):
            print(" " * x, end="")
            for col in range(self.width):
                print("#", end="")
            print()


    def __str__(self):
        """ returns the string representation of Rectangle instance """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    @staticmethod
    def setter_validator(attr, value):
        """ validates the value inputs into the attributes """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attr))
        if attr == "x" or attr == "y":
            if value < 0:
                raise ValueError("{} must be > 0".format(attr))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attr))
