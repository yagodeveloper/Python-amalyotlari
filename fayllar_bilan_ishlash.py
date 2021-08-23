# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 14:07:24 2021

@author: Admin
"""

with open('pi.txt') as file:
    pi = file.read()



print(pi)




pi = pi.rstrip()
pi = pi.replace("\n", '')
pi = float(pi)
print(pi)