#!/usr/bin/python3
"""
input output
"""
import json


def to_json_string(my_obj):
    """
    returns the JOSC represantation of an object
    """
    return json.dumps(my_obj)
