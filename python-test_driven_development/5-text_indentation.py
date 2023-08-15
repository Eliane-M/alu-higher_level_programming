#!/usr/bin/python3
"""
prints a text with 2 lines after . or ? or :
"""


def text_indentation(text):
    """
    text should be a string
    if its not a string raise a type error
    there should be no spaces at the beginning or the end of the line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
