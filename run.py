#!/usr/bin/env python3
import os
import requests
import json


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
            # print(line)

            # add fields to item dictionary
            if desc == 0:
                line = line.strip()
                item_dict[item_fields[desc]] = line
            elif desc == 1:
                # convert weight string to integer
                line = int(line[0:4].strip())
                item_dict[item_fields[desc]] = line
            elif desc == 2:
                # add description to dict
                item_dict[item_fields[desc]] = line.strip()
                # add image name dict
                name = file[0:3] + '.jpeg'
                # print(f'File: {name}')
                item_dict[item_fields[desc+1]] = name

            # go to next item in file
            desc += 1

        # post each file to site

        # serialize Python object into json notation
        item_jason = json.dumps(item_dict)
        response = requests.post('http://', data = item_jason)

