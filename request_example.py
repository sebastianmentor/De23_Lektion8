import requests
import json


data = requests.get('https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16.158/lat/58.5812/data.json')
print(data.json())

for key in data.json():
    print(key)