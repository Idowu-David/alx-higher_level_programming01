#!/usr/bin/python3
""" Square Class """


class Square:
    """ defines a square class """
    def __init__(self, size=0, position=(0, 0)):
        """ initializer """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ position getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ position setter """
        if type(value) is not tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ returns the current square area """
        return self.size * self.size

    def my_print(self):
        """ prints the square with the character # """
        if self.size == 0:
            print()
        sq_x, sq_y = self.position[0], self.position[1]
        for _y in range(sq_y):
            print()
        for row in range(self.size):
            print(" " * sq_x, end="");
            for col in range(self.size):
                print("#", end="")
            print()
