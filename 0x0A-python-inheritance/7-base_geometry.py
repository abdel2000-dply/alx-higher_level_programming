#!/usr/bin/python3
"""module Geometry"""


class BaseGeometry:
    """class representing base geometry"""

    def area(self):
        """raises an Exceptionan Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as an integer greater than 0"""
        if isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
