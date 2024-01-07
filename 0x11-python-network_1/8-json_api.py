#!/usr/bin/python3
""" Search API """
import requests
from sys import argv


if __name__ == "__main__":

    q = argv[1] if len(argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user" 
    data = {'q': q}
    response = requests.post(url, data)
    try:
        json_resp = response.json()
        if json_resp:
            print(f'[{json_resp.get("id")}] {json_resp.get("name")}')
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")

