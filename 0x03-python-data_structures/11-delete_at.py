#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return my_list
        new = my_list.copy()
        del new[idx]
        return new
    return my_list
