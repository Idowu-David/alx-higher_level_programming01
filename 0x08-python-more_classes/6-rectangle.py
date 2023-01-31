#!/usr/bin/python3
""" this module defines a rectangle class """


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ initialisation of width and height attribute of rectangle """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        number_of_instances += 1

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ returns a printable representation of rectangle """
        rect = ""
        count = 0
        if self.width == 0 or self.height == 0:
            return rect
        for row in range(self.height):
            for col in range(self.width):
                rect += "#"
            count += 1
            if count < self.height:
                rect += "\n"
        return rect

    def __repr__(self):
        """ returns a string representation of rectangle"""
        rect = "Rectangle({}, {})".format(self.width, self.height)
        return rect

    def __del__(self):
        """ detects when an instance is deleted """
        number_of_instances -= 1
        print("Bye rectangle...")
