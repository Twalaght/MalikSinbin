#!/usr/bin/python3

import argparse
import configparser
import os
import re
import urllib.request
from requests import get
from viewer import slideshow

# Read the arguments given to the script
parser = argparse.ArgumentParser(description="Index and display images from derpibooru")
parser.add_argument("-s", metavar="search", type=str, help="Search for a specific tag")
parser.add_argument("-t", action="store_true", help="Reindex image tags")
args = parser.parse_args()

# Read the config file from the working directory
config = configparser.ConfigParser()
config.read("config.txt")
image_dir = config.get("der.py", "image_dir")

# Create a dictionary for each images ID to its file path
def file_search():
    # Create an empty dictionary to add entries to
    ID_paths = {}

    # Walk each folder in the given directory
    for root,dirs,file in os.walk(image_dir):
        for name in file:
            # Extract the full file path of each image
            full_path = os.path.join(root, name)

            # Extract the image number from the full path
            ID = re.search(r"\d+__", full_path).group()[:-2]

            # Combine the path and ID into a dictionary
            ID_paths[int(ID)] = full_path

    return ID_paths

# Read the cached image tags in
def tags_read():
    file = open("tags.txt", "r", encoding="utf-8")
    cache = eval(file.read())
    file.close()
    return cache

# Write a tag dictionary to the cache file
def tags_write(cache):
    file = open("tags.txt", "w", encoding="utf-8")

    # Write an opening brace on its own line
    file.write("{\n")

    # Write each dictionary entry on its own line
    for index in range(len(cache)):
        temp = list(cache)[index]
        file.write(str(temp) + ": " + str(cache[temp]))

        # For every line but the last, write the comma
        if index != len(cache) - 1:
            file.write(",\n")

    # Finish the file with a closing brace
    file.write("\n}")
    file.close()

# Save all available image tags to a cached text file
def tag_index():
    # Read in all image IDs, and the current tag cache
    imageIDs = list(file_search().keys())
    cache = tags_read()

    # Write a dictionary entry for each ID to its corresponding path
    for index in range(len(imageIDs)):
        if imageIDs[index] not in cache:
            # Print a status message for each image
            print("Tagging image " + str(imageIDs[index]) + "... ", end = "")

            try:
                # Send a get request to the server for the images json file
                request = get("https://derpibooru.org/api/v1/json/images/" + str(imageIDs[index]))

                # If status code is not okay, back off on the requests
                if request.status_code != 200:
                    print("Failed! \n Request failed, gracefully backing off")
                    tags_write(cache)
                    break

                # Extract the images takes from the json file and add it to the cache
                tags = request.json()["image"]["tags"]
                cache[imageIDs[index]] = tags
                print("Done")

            except:
                # Print a failed message and flush the cache if a tag lookup fails
                print("FAILED")
                tags_write(cache)
    
    # If all else succeeds, write the cache to disk
    tags_write(cache)

if(args.s):
    # Read the paths, cached tags, and create an empty list for final images
    paths = file_search()
    tags = tags_read()
    final_images = []

    # Check each images tags for a match to the search
    # Adds to the final images if matched
    for index in range(len(tags)):
        img_ID = list(tags)[index]
        if args.s in tags[img_ID]:
            final_images.append(paths[img_ID])

    # Shuffle the images, and start the slideshow with them
    # random.shuffle(final_images)
    slideshow(final_images, 5000)

elif (args.t):
    tag_index()

# TODO - Multiple search processing
# TODO - Resize very wide images properly
# TODO - Implement sequences wrapping
# TODO - Progress when tagging