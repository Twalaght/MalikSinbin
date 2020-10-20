#!/usr/bin/python3

from pathlib import Path
import os
import json



# TODO - Set this in the actual home folder and make path friendly
# TODO IF FILE EXISTS THAT IS
with open("playlist.json") as file:
      playlists = json.load(file)

# print(playlists)
# exit()


dict = {}
songs = []


music_path = Path("/mnt/c/Users/Jono/Desktop/Music")

# music_path = Path("/mnt/f/Media/Music/")


# print(music_path.exists())


for path, subdir, files in os.walk(music_path):
    # print('Found directory: %s' % dirName)
    for file in files:
        # ext = os.path.splitext(fname)[1]
        # TODO - Keep extensions and cut them when we print
        songs.append(os.path.splitext(file)[0])

print(songs)


for song in songs:
    # print(song)
    dict[song] = [False] * 5

print("Dictionary is ")
print(dict)


# TODO - Write to playlist file
# a_file = open("playlist.json", "w")
# json.dump(dict, a_file)
# a_file.close()
