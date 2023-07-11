#!/usr/bin/python3
"""Module read file"""


def read_file(filename=""):
    """Read file func"""
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end='')
