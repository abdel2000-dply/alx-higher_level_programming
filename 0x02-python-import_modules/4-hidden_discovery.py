#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    name_list = dir(hidden_4)
    for name in name_list:
        if not name.startswith('__'):
            print(name)
