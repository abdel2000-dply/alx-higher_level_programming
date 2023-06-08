#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ar = sys.argv[1:]
    arl = len(ar)

    if arl == 0:
        print("0 arguments.")
    else:
        print("{} {}:".format(arl, "argument" if arl == 1 else "arguments"))
        for i in range(arl):
            print("{}: {}".format(i + 1, ar[i]))
