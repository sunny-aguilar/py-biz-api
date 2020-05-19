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
directory = './supplier-data/images'

# iterate over files in directory
for file in os.listdir(directory):

    if file.endswith('.tiff'):

        # file location and name
        file_loc = './supplier-data/images/'

        # open the file
        img = Image.open(file_loc + file)

        # resize image
        newsize = (600, 400)
        img = img.resize(newsize)

        # save file
        save_location = './supplier-data/images/' + file
        img.convert('RGB').save(save_location, 'JPEG')

        # rename files
        new_name = file
        new_name = new_name[0:3] + 'jpeg'
        os.rename(directory+'/'+file, directory+'/'+new_name)