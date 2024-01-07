#!/usr/bin/python3
""" Time for an interview! """
import requests
from sys import argv


if __name__ == "__main__":

    repo, owner = argv[1], argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {"per_page": 10}

    commits = requests.get(url, params=params).json()

    for commit in commits:
        name = commit.get("commit").get("author").get("name")
        print(f'{commit.get("sha")}: {name}')
