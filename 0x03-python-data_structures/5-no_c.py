#!/usr/bin/python3


def no_c(my_string):
    if my_string:
        new = ""
        for c in my_string:
            if 'c' == c or 'C' == c:
                continue
            new += c
        return new
    return my_string
