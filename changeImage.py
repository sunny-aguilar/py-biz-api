#!/usr/bin/env python3
#
#   This script implements a simple email client to prepare an email for
#   sending. The email and SMTP modules are used as the workhorses behind the
#   email and the OS module is used to work with the Operating System.
#
#
#   Author:     Sandro Aguilar
#   Date:       May 18, 2020
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os, sys, PIL
from PIL import Image

# directory to iterate over
directory = './supplier-data'

# iterate over files in directory
for file in os.listdir(directory):

    if not file.endswith('.DS_Store'):
        # file location and name
        file_loc = './images/'

        # open the file
        img = Image.open(file_loc + file)

        # resize image
        newsize = (600, 400)
        img = img.resize(newsize)

        # save file
        save_location = './supplier-data/' + file + '.tiff'
        img.convert('RGB').save(save_location)