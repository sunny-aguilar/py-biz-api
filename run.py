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

item_fields = ['name', 'weight', 'description', 'image_name']

# open each text file
for file in files:
    with open(directory+file, 'r+') as current_file:
        desc = 0
        for line in current_file:
            # remove trailing space and linefeed/carriage returns
            field = line.strip()
            print(field)

            # add fields to item dictionary
            if desc == 1:
                line = line[-3:0]
                line = line.strip()
                print(f'Line: {line}')
                item_dict[item_fields[desc]] = line
            else:
                item_dict[item_fields[desc]] = line

            # go to next item in file
            desc += 1
