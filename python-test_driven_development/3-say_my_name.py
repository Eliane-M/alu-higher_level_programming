#!/usr/bin/python3
"""
Prints 'My name is' with the first_name and the second_name
"""


def say_my_name(first_name, last_name=""):
    """
    both names should be strings
    raise a type error if they are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a '
                'string or last_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('first_name must be a '
                'string or last_name must be a string')
    print('My name is ' + first_name + last_name)
