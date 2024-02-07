#!/usr/bin/python3
"""  POST an emai """
import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
