#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    val = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

    res = 0
    l = len(roman_string)
    for i in range(l):
        if roman_string[i] not in val:
            return 0
        if i < l - 1 and val[roman_string[i]] < val[roman_string[i + 1]]:
            res -= val[roman_string[i]]
        else:
            res += val[roman_string[i]]

    return res
