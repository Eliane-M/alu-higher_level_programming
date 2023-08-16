#!/usr/bin/python3
"""
manage id attribute for all future classes
and to avoid duplicating code
"""


class Base:
    """
    the base code for all the projects in almost_a_circle
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
