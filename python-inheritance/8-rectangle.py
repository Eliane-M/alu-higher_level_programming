#!/usr/bin/python3
"""
inheritance
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
basegeometry
"""


class Rectangle(Basegeometry):
    """
    class
    """
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
