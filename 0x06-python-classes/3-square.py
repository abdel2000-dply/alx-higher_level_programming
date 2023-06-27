#!/usr/bin/python3
"""This is a module containing a square"""


class Square:
    """This is a Square.

    Attributes:
        __size (int): the size of sq.
    """

    def __init__(self, size=None):
        """Instance

        Args:
            size (int): size of sq.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area"""
        return self.__size ** 2
