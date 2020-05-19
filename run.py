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

            # add fields to item dictionary
            if desc == 1:
                # convert weight string to integer
                line = int(line[0:4].strip())
                item_dict[item_fields[desc]] = line
            elif desc == 4:
                # add image name dict
                name = file[0:3] + 'jpeg'
                item_dict[item_fields[desc]] = name
            else:
                item_dict[item_fields[desc]] = line.strip()

            # go to next item in file
            desc += 1

        # print(line)
        print(item_dict)

