#!/usr/bin/python3
"""This is a module containing a square"""


class Square:
    """This is a Square.

    Attributes:
        __size (int): the size of sq.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Instance

        Args:
            size (int): size of sq.
            position (tupl): position of sq.
        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """Return position"""
        return self.__position

    @position.setter
    def position(self, n):
        """position setter"""
        if type(n) is not tuple or len(n) != 2 or \
                type(n[0]) is not int or type(n[1]) is not int or \
                n[0] < 0 or n[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = n

    def area(self):
        """Return area"""
        return self.__size ** 2

    def my_print(self):
        """Print the sq using '#'"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
