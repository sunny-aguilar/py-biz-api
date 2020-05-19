#!/usr/bin/env python3
import os
import requests


# directory of description files
directory = './supplier-data/descriptions/'
files = os.listdir(directory)

# upload URL
url = 'http://35.225.164.210/fruits'


item_dict = {
    'name': '',
    'weight': 0,
    'description': '',
    'image_name': ''
}


# open each text file
for file in files:
    with open(directory+file, 'r+') as current_file:
        for line in current_file:
            # remove trailing space and linefeed/carriage returns
            field = line.strip()
            print(field)

            # add field to item dictionary

