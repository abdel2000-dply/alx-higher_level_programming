#!/usr/bin/python3
"""MagicClass"""
import math


class MagicClass:
    """Init Class"""
    def __init__(self, radius=0):
        """Init MagicClass"""
        self.__radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """The area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """The circumference"""
        return 2 * math.pi * self.__radius
