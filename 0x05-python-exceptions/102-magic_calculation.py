#!/usr/bin/python3

def magic_calculation(a, b):
    res = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('too far')
            res += (a ** b) / i
        except Exception:
            res = a + b
            break
    return res
