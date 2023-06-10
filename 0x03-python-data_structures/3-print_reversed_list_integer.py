#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
	rev = my_list.copy()
        rev = rev.reverse()
        for i in rev:
            print("{:d}".format(rev[i]))
