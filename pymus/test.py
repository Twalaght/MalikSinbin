#!/usr/bin/python3

import json

dictionary_data = {"Soft Fuzzy Man": ["Krump", "Kek"], "b": 2}

a_file = open("data.json", "w")
json.dump(dictionary_data, a_file)
a_file.close()

a_file = open("data.json", "r")
output = a_file.read()
print(output)
a_file.close()
