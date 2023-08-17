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
        """
        super id class
        assign width, height, x, and y to right attributes
        """
        super().__innit__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        private instance for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        self.__width = value

    @property
    def height(self):
        """
        height private instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        self.__height = value

    @property
    def x(self):
        """
        private instance for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        """
        self.__x = value

    @property
    def y(self):
        """
        private instance for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """
        self.__y = value
