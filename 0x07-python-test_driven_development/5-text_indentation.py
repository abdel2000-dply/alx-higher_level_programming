#!/usr/bin/python3
"""Module: text indentation"""


def text_indentation(text):
    """Text indentation func"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_l = [lines.strip(' ') for lines in text.split('\n')]
    res = "\n".join(list_l)
    print(res, end="")
