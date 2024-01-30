#!/usr/bin/python3
""" POST an email #1 """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    response = requests.post(url, {'email': email})
    print(response.text)
