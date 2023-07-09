#!/usr/bin/python3
"""Module max integer"""


def max_integer(list=[]):
	"""Max integer func"""
    if len(list) == 0:
        return None
    res = list[0]
    i = 1
    while i < len(list):
        if list[i] > res:
            res = list[i]
        i += 1
    return result
