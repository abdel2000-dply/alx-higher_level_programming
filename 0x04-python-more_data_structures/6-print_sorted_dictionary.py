#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary.keys())
    for key in new:
        print("{}: {}".format(key, new[key]))
