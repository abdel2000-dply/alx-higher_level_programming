#!/usr/bin/python3
"""Module inherits from"""


def inherits_from(obj, a_class):
    """inherits from"""
    return isinstance(obj, a_class) and type(obj) != a_class
