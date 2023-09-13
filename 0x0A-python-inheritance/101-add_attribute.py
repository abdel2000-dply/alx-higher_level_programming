#!/usr/bin/python3
"""Can I?"""


def add_attribute(obj, attribute, value):
    """add attribut function"""

    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
