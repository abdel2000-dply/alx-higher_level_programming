#!/usr/bin/python3
""" Rectangle Class """
from .base import Base


class Rectangle(Base):
    """ Rectangle Class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instance"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        pass

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        pass

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        pass

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        pass
