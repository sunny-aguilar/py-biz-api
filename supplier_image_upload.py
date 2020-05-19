#!/usr/bin/env python3
import requests, os


url = "http://localhost/upload/"

with open('/supplier-data/images', 'rb') as opened:
    if opened.endswith('.jpeg'):
        r = requests.post(url, files={'file': opened})


# directory to iterate over
directory = './supplier-data/images'

# iterate over files in directory
for file in os.listdir(directory):
    # if file.endswith('.jpeg'):
    #     r = requests.post(url, files={'file': file})
    with open('./supplier-data/images/'+file, 'rb') as opened:
        if file.endswith('.jpeg'):
            r = requests.post(url, files={'file': opened})