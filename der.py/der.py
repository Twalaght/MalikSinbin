#!/usr/bin/python3

import argparse
import configparser
import os
# TODO - from pathlib import Path
import re
import urllib.request
from requests import get


# Read the arguments given to the script
parser = argparse.ArgumentParser(description="Index and display images from derpibooru")
parser.add_argument("-s", metavar="search", type=str, help="Search for a specific tag")
parser.add_argument("-f", action="store_true", help="Reindex image paths")
parser.add_argument("-t", action="store_true", help="Reindex image tags")
args = parser.parse_args()

# Read the config file from the working directory
config = configparser.ConfigParser()
config.read("config.txt")
image_dir = config.get("der.py", "image_dir")


# Extract the path and ID of each image in the folder
def filewalk():
    # Create two empty lists to eventually return
    paths, imageIDs = [], []

    # Walk each folder in the given directory
    for root,dirs,file in os.walk(image_dir):
        for name in file:
            # TODO - Os.path.join may be wonky
            paths.append(os.path.join(root, name))

    # Walk the files for each folder and add thier IDs
    for path in paths:
        ID = re.search(r"\d+__", path).group()[:-2]
        imageIDs.append(ID)

    return paths, imageIDs

# Save the image paths to a text file
def writepaths(paths, imageIDs):
    file = open("paths.txt", "w", encoding="utf-8")

    # Write the opening brace on its own line
    file.write("{\n")

    # Write a dictionary entry for each ID to its corresponding path
    for index in range(len(imageIDs)):
        file.write("\"" + imageIDs[index] + "\": \"" + paths[index] + "\"")
        # For every line but the last, write the comma
        if index != len(imageIDs) - 1:
            file.write(",\n")

    # Finish the file with a closing brace
    file.write("\n}")
    file.close()


if(args.f):
    paths, imageIDs = filewalk()
    writepaths(paths, imageIDs)


def readtags():
    file = open("tags.txt", "r", encoding="utf-8")
    index = eval(file.read())
    file.close()
    return index


# NEED TO APPEND TO DICTIONARY THEN CALL A SEPARATE WRITE CALL
# Save the image tags to a text file
def tagindex(imageIDs, cache):
    file = open("tags.txt", "w", encoding="utf-8")

    # Write the opening brace on its own line
    file.write("{\n")

    # Write a dictionary entry for each ID to its corresponding path
    for index in range(len(imageIDs)):

        if str(index) not in cache:
            print("Tagging image " + str(imageIDs[index]) + "...")

            request = get("https://derpibooru.org/api/v1/json/images/" + str(imageIDs[index]))

            if request.status_code != 200:
                print("Request failed, gracefully backing off")
                break

            tags = request.json()["image"]["tags"]

            file.write("\"" + imageIDs[index] + "\": \"" + str(tags))
            # For every line but the last, write the comma
            if index != len(imageIDs) - 1:
                file.write(",\n")

    file.write("\n}")
    file.close()



#paths, imageIDs = filewalk()
#tagindex(imageIDs, readtags())




import tkinter as tk
from PIL import ImageTk, Image

# Display a slideshow of the given images, with a delay for each
def slideshow(images, delay):
    def next_image():
        # Open the image, read in its size, and calculate the scale
        input_image = Image.open(next(img_iter))

        # Get image dimensions and scale it to fit screen
        dims = list(input_image.size)
        dims = [int(dims[0] * viewer.winfo_screenheight() / dims[1]), viewer.winfo_screenheight()]

        # Set the image into the displays label
        img_label.img = ImageTk.PhotoImage(input_image.resize((dims), Image.ANTIALIAS))
        img_label.config(image = img_label.img)
        img_label.after(delay, next_image)

    # Sets up the iterator, labels, and slideshow config
    img_iter = iter(images)
    viewer = tk.Tk()
    viewer.config(background="#222222")
    viewer.attributes("-fullscreen", True)
    img_label = tk.Label(viewer)
    img_label.pack()

    # Call next image once to start recursion, and run the main loop
    next_image()
    viewer.mainloop()

if (args.s == "ss"):
    paths, imageIDs = filewalk()
    import random
    random.shuffle(paths)
    slideshow(paths, 3000)