#!/usr/bin/python3
""" print_sorted list module """


class MyList(list):
    """ defines MyList class """
    def print_sorted(self):
        """ prints the list object in a sorted order """
        new_list = sorted(self)
        print(new_list)
