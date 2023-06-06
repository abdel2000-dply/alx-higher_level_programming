#!/usr/bin/python3
for c in range(97, 123):
    if chr(c) in ('q', 'e'):
        continue
    print("{}".format(chr(c)), end="")
