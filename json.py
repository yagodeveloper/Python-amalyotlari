# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 15:35:40 2021

@author: Admin
"""

import json
import googlemaps
from apikey import APIKEY
gmaps = googlemaps.Client(key=APIKEY)
geocode_result = gmaps.geocode('okdaryo','samarkand','ozbekistan')
g=json.dumps(geocode_result[0],indent=4,sort_keys = True)
print(g)