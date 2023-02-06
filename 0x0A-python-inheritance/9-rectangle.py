#!/usr/bin/python3
""" defines BaseGeometey class and Rectangle class(subclass) """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the `value` passed by the user """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ initialisation """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ calculates the area of the Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ string representation of Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
