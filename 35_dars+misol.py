# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 23:39:51 2021

@author: Admin
"""

# import json
# files = ["talaba1.json","talaba2.json","talaba3.json","talaba4.json"]
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#             # print(f"{filename} mavjud emas")
#             pass #hech narsa bajarmaslikni buyuradigan operator
#     else:
#         print(talaba['ism'])
        
  
        
n= input("son kiriting")
try:
    n= int(n)
    x=20/n
except ValueError:
    print("BUtun son kiriting")
except ZeroDivisionError:
    print("0 ga bo'lish mumkin emas")
else:
    print(f"x={x}")