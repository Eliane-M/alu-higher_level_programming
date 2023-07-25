#!/usr/bin/python3
"""
checks if the size of square is an integer and > than 0
"""


class Square:
    """
    class instances
    """
    def __init__(self, size=0):
        self.__size = size
        if size != {:d}:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
