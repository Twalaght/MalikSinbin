#!/usr/bin/python3

import base64
import time
import argparse
from requests import get
import urllib.request
import configparser

# Read the arguments given to the script
parser = argparse.ArgumentParser(description="Download a pool of images from e621")
parser.add_argument("pool_id", metavar="Pool_ID", type=str, help="Pool of images to download (Ex: 11686)")
parser.add_argument("name", metavar="Name", type=str, help="Name template to use when saving the images")
args = parser.parse_args()

# Read the config file from the working directory
config = configparser.ConfigParser()
config.read("config.txt")

# Set all relevant configuration variables
user_agent = config["e621"]["user_agent"]
user_name = config["e621"]["user_name"]
API_key = config["e621"]["API_key"]

# Calculate the basic auth b64 credential
user_auth = (user_name + ":" + API_key).encode("ascii")
b64_auth = "Basic " + base64.b64encode(user_auth).decode("ascii")

# Set the required header for all API requests
headers = {"User-Agent": user_agent, "Authorization": b64_auth}

# Get all the post IDs belonging to the pool
pages = get("https://e621.net/pools/" + args.pool_id + ".json", headers=headers).json()["post_ids"]
time.sleep(1.5)

# Download each page in the pool
for page in range(len(pages)):
    # Status message
    print("Parsing page " + str(page + 1) + "...")

    # Get the source for each individual image
    image = get("https://e621.net/posts/" + str(pages[page]) + ".json", headers=headers).json()["post"]["file"]["url"]
    time.sleep(1.5)

    # Get the file extension of the image
    extension = "." + image.split(".")[-1]

    # Write the image to disk
    urllib.request.urlretrieve(image, args.name + " " + str(page + 1).zfill(len(str(len(pages)))) + extension)
    time.sleep(1.5)