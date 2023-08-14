#!/usr/bin/python3
"""
This function adds tow integers
b is initially assigned to 98
a and b must be integers
"""


def add_integer(a, b=98):
    """
    if a or b are not integers raise a TypeError
    if a or b are float they should be first casted into an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return (a + b)
