# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:27:14 2021

@author: Admin
"""

import requests
from pprint import pprint
import json

# sahifa = "https://kun.uz/news/main"
#r=requests.get(sahifa)
# pprint(r.text)

country = 'uzbekistan'
url = f"https://restcountries.eu/restv2/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
pprint(r_json["capital"])
