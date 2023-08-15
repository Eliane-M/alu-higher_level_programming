#!/usr/bin/python3
"""
prints a square with the # character
"""


def print_square(size):
    """
    size is the size of the square
    raise a type error if size is not an integer
    raise a value error if size is less than zero
    if size is a float and less than zero raise a value error
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
 
    if size == 0:
        print()
    else:
        for _ in range(size):
            print('#' * size)
