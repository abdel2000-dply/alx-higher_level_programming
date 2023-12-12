#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    ar = sys.argv

    if len(ar) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(ar[1])
    op = ar[2]
    b = int(ar[3])

    res = 0

    if op == '+':
        res = add(a, b)
    elif op == '-':
        res = sub(a, b)
    elif op == '*':
        res = mul(a, b)
    elif op == '/':
        res = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, op, b, res))
    sys.exit(0)
