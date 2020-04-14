#!/usr/bin/python3

import configparser
import os
# from pathlib import Path
import re
import urllib.request
from requests import get

# Read the config file from the working directory
# config = configparser.ConfigParser()
# config.read("config.txt")
# image_dir = config.get("der.py", "image_dir")


# TODO - Name and tidy all this up
# Extract the path and ID of each image in the folder
# paths = []
# imageIDs = []
# def filewalk():
#     for root,dirs,file in os.walk(image_dir):
#         for name in file:
#               paths.append(os.path.join(root, name))

#     for path in paths:
#         ID = re.search(r"\d+__", path).group()[:-2]
#         imageIDs.append(ID)

# filewalk()

# f = open("paths.txt", "w")
# f.write("{\n")
# for index in range(len(imageIDs)):
#     f.write("\"" + imageIDs[index] + "\": " + "\"" + paths[index] + "\"")
#     if index != len(imageIDs) - 1:
#         f.write(",\n")

# f.write("\n}")
# f.close()




# TODO - TEST TAG GRABBING
# tags = get("https://derpibooru.org/api/v1/json/images/" + str(imageIDs[0])).json()["image"]["tags"]
# print(type(tags))
# print(tags) 

# TODO - TEST TAG WRITING
# f = open("tags.txt", "w")
# f.write("{\n")
# f.write("\"" + imageIDs[0] + "\": " + str(tags))
# f.write("\n}")
# f.close()

# TODO - OPENS TAGS, USED FOR INDEXING AND WRITING
# file = open("tags.txt", "r")
# dictionary = eval(file.read())
# file.close()

# test = dictionary["1013621"]
# print(type(test))
# print(test)





# from itertools import cycle
# import tkinter as tk
# from PIL import ImageTk, Image

# class Viewer(tk.Tk):
#     # Initialize the image viewer
#     def __init__(self, input_images, delay):
#         # Setup the photo viewer
#         tk.Tk.__init__(self)
#         self.title("DisplayBooru")
#         self.delay = delay * 1000
#         self.config(background="#222222")
#         self.attributes("-fullscreen", True)

#         # Read in the input images and resize them as needed
#         arry = []
#         for image in input_images:
#             # Read in an image and get its size values
#             input_image = Image.open(image)
#             width, height = input_image.size

#             # Rescale the image to fit the screen
#             scale = self.winfo_screenheight() / height
#             width = (int)(width * scale)
#             height = (int)(height * scale)
#             input_image = input_image.resize((width, height), Image.ANTIALIAS)

#             # Add the image into the array
#             arry.append(ImageTk.PhotoImage(input_image))

#         # Finalize the tk setup
#         self.pictures = cycle(arry)
#         self.picture_display = tk.Label(self)
#         self.picture_display.pack()

#     def slideshow(self):
#         # Iterates through the images given, showing each for delay time
#         img_object = next(self.pictures)
#         self.picture_display.config(image=img_object)
#         self.after(self.delay, self.slideshow)

#     def run(self):
#         self.mainloop()


# delay = 5
# images = ["1.png", "2.jpeg", "3.png"]

# app = Viewer(images, delay)
# app.slideshow()
# app.run()