#!/usr/bin/python3
"""
class rectangle that inherits from base
"""
from models.base import Base


class Rectangle:
    """
    class attributes and methods
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__innit__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('Width must be an integer')
        if value <= 0:
            raise TypeError('Width very small')
        self.__width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('Height has to be integer')
        if value <= 0:
            raise TypeError('Height value so small')
        self.__height = value

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x value too small')
        self.__x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise ValueError('y must be an integer')
        if value < 0:
            raise ValueError('y cannot be negative')
