#!/usr/bin/env python3
import requests, os

# upload location
url = "http://localhost/upload/"


# directory of jpeg images
directory = './supplier-data/images/'

# iterate over files in directory
for file in os.listdir(directory):
    # open and upload each image
    with open('./supplier-data/images/'+file, 'rb') as opened:
        if file.endswith('.jpeg'):
            r = requests.post(url, files={'file': opened})