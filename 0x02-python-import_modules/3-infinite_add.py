#!/usr/bin/python3
import sys
if __name__ == "__main__":
    ar = sys.argv[1:]
    sum = 0
    for i in range(len(ar)):
        sum += int(ar[i])

    print(sum)
