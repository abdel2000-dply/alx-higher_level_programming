#!/usr/bin/python3
for n in range(10):
    for m in range(n + 1, 10):
        print("{}{}".format(n, m), end="")
        if n != 8 or m != 9:
            print(", ", end="")
        else:
            print()
