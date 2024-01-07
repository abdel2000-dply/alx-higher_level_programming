#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    if list_of_integers:
        low, high = 0, len(list_of_integers) - 1
        while low < high:
            mid = (low + high) // 2

            if list_of_integers[mid] > list_of_integers[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return list_of_integers[low]
    return None
