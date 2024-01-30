#!/usr/bin/python3
""" My GitHub! """
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username, passw = argv[1], argv[2]

    response = requests.get(url, auth=(username, passw))
    print(response.json().get("id"))
