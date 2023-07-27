#!/usr/bin/python3
"""
checks if the size of square is an integer and > than 0
"""


class Square:
    """
    class instances
    """
    def __init__(self, size=0):
        """
        Initialise a square object with a given size
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
