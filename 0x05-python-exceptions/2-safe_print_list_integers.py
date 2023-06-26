#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            print("{:d}".format(i), end=" ")
            count += 1
            if count = x:
                break
        except (ValueError, TypeError):
            continue
    print()
    return count
