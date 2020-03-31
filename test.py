#!/usr/bin/python3

import requests

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)



response = requests.get("https://derpibooru.org/api/v1/json/images/2308699")
print(response.status_code)
print(response)
jprint(response.json())