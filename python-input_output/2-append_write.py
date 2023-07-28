#!/usr/bin/python3
"""
input output
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a string
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
