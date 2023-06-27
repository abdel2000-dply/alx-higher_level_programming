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
        self.__size = size
