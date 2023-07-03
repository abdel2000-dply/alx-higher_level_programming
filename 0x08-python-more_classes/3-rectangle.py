#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Class rectangle"""
    def __init__(self, width=0, height=0):
        """Init a rectangle object."""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (not self.__width or not self.__height):
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if (not self.__width or not self.__height):
            return ""
        return "\n".join(["#" * self.__width] * self.__height)
