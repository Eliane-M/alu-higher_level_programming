#!/usr/bin/python3
"""
inheritance
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """
    square classes
    """
    def __init__(self, size):
        """
        initialization
        """
        self.__size = self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
