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
        raise TypeError('text must be a string')
    separators = ['.', '?', ':']
    lines = text.splitlines()
    formatted_lines = []

    for line in lines:
        line = line.strip()
        if any(sep in line for sep in separators):
            formatted_lines.append(line)
            formatted_lines.append("")
        else:
            formatted_lines.append(line)

    print('\n'.join(formatted_lines))
