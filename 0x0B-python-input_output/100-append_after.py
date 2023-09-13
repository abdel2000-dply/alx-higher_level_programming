#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """append after a choosing string"""

    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
