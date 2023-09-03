#!/usr/bin/python3
"""Module: Print Square"""


def print_square(size):
    """print square func"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size if size > 0 else "")
