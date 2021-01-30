#!/usr/bin/python3

import argparse
import base64
import configparser
import time

# TODO
import urllib.request
import urllib.parse

from pathlib import Path
from requests import get

# Read the arguments given to the script
parser = argparse.ArgumentParser(description="Download images from e621 from a tag or pool")
parser.add_argument("target", metavar="tag/pool", type=str, help="tag or pool to download (Ex: anthro, 11686)")
parser.add_argument("-t", "--title", type=str, help="set the title when downloading a pool")
parser.add_argument("-l", "--limit", type=int, help="set the limit for how many images to download")
args = parser.parse_args()

# Set up the config parser and read in the auths file if it exists
config = configparser.ConfigParser()
auths = Path.home() / ".config" / "auths.txt"
if auths.exists():
    config.read(auths)
else:
    print(f"Authentication not found at {auths}, please create it")
    exit()

# Set all relevant configuration variables
user_agent = config.get("e621", "user_agent")
user_name = config.get("e621", "user_name")
API_key = config.get("e621", "API_key")

# Calculate the basic auth b64 credential and set the required request header
user_auth = (user_name + ":" + API_key).encode("ascii")
b64_auth = "Basic " + base64.b64encode(user_auth).decode("ascii")
headers = {"User-Agent": user_agent, "Authorization": b64_auth}

# Check if the target is a pool or tag, and url encode it if it is a tag
pool = True
if not args.target.isnumeric():
    pool = False
    args.target = urllib.parse.quote_plus(args.target)



# TODO


# Get all the post IDs belonging to the target query

# Pool
# pages = get(f"https://e621.net/pools/{args.target}.json", headers=headers).json()["post_ids"]

# Tag
pages = get(f"https://e621.net/posts.json?tags={args.target}", headers=headers).json()["posts"]
print(pages)

lastid = pages[-1]["id"]
exit()


time.sleep(1.5)

# Create the required folder with the given name
Path(args.name).mkdir(parents=True, exist_ok=True)

# Print an opening status message for the pool
print(f"[Started downloading {args.name}]")


print(args.target)
print(args.target.isnumeric())
exit()



# Download each page in the pool
for page in range(len(pages)):
    # Print a status message for each page
    print(f"Downloading page {str(page + 1)} of {str(len(pages))}...")

    # Get the source for each individual image
    image = get(f"https://e621.net/posts/{str(pages[page])}.json", headers=headers).json()["post"]["file"]["url"]
    time.sleep(1.5)

    # Generate the file path for each image to be saved to
    img_path = Path.cwd() / args.name / (args.name + " " + str(page + 1).zfill(len(str(len(pages)))) + Path(image).suffix)

    # Write the image to disk
    urllib.request.urlretrieve(image, img_path)
    time.sleep(1.5)

# Print a final status when all downloads are finished
print(f"[Finished downloading {args.name}]")




# Add support for downloading tags instead of pools
# Automatic pool naming unless an override is given
# Regex to determine is we are using a tag or pool
# File renaming for tags inline with e6db\
# Download limit numbers
# Ability to roll more than one tag in [might be hard, maybe only useful for order:score], need to escape space
# Waiting... done for downloads, could delete previous line instead if possible
