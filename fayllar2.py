# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 14:38:37 2021

@author: Admin
"""

filename = 'talablar.txt'
with open(filename) as file:
    for line in file:
        print(line)
        
with open(filename) as file:
    talablar = file.readlines()
    
print(talablar)    

