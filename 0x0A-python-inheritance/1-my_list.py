#!/usr/bin/python3
"""Module print_sorted"""


Class MyList(list):
	"""Class"""
    def print_sorted(self):
        """the list sorted in ascending order"""
	sorted_list = sorted(self)
        print(sorted_list)
