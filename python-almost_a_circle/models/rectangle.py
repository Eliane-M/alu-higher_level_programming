#!/usr/bin/python3
"""
class rectangle that inherits from base
"""
from models.base import Base


class Rectangle(Base):
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
        self.__width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        self.__y = value
