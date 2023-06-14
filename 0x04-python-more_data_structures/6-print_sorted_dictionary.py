#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary.keys())
    for k in new:
        print("{}: {}".format(k, new[k]))
