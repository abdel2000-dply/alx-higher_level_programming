#!/usr/bin/python3
""" Error code #1 """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    resp = requests.get(url)
    if resp.status_code >= 400:
        print("Error code:", resp.status_code)
    else:
        print(resp.text)
