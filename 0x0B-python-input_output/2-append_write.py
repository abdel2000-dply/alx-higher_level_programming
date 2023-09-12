#!/usr/bin/python3
"""Module append"""


def append_write(filename="", text=""):
    """append write func"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
