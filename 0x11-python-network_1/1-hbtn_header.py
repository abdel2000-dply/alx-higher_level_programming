#!/usr/bin/python3
""" Response header value """
from sys import argv
import urllib.request


if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.info()["X-Request-Id"])
