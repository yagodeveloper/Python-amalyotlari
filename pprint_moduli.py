# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 19:06:54 2021

@author: Admin
"""

from pprint import pprint
import json
# filename = 'bemor.json'
# with open(filename) as f:
#     bemor = json.load(f)
# pprint(bemor)

import requests
r = requests.get('https://api.github.com')
pprint(r.json())