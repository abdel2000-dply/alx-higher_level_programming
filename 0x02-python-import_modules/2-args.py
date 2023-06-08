#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ar = sys.argv[1:]
    ar_len = len(ar)

    if ar_len == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(ar_len))
        for i in range(ar_len):
            print("{}: {}".format(i + 1, ar[i]))
