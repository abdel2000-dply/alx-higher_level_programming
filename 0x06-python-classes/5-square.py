#!/usr/bin/python3
"""This is a module containing a square"""


class Square:
    """This is a Square.

    Attributes:
        __size (int): the size of sq.
    """

    def __init__(self, size=0):
        """Instance

        Args:
            size (int): size of sq.
        """
        self.__size = size

    @property
    def size(self):
        """Return size of sq."""
        return self.__size

    @size.setter
    def size(self, n):
        """Size setter"""
        if type(n) is not int:
            raise TypeError("size must be an integer")
        if n < 0:
            raise ValueError("size must be >= 0")
        self.__size = n

    def area(self):
        """Return area"""
        return self.__size ** 2

    def my_print(self):
        """Print the sq using '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
