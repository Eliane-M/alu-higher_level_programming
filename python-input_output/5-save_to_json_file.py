#!/usr/bin/python3
"""
input and output
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write an object to a text file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
