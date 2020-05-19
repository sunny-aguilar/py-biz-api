#!/usr/bin/env python3
import requests


url = "http://localhost/upload/"
with open('/supplier-data/images', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
