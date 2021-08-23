# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 01:37:18 2021

@author: Admin
"""

def bahola(ismlar):
    baholar={}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"talaba {ism.title()}ni bahosini kiriting")
        baholar[ism]=int(baho)
    return baholar
talabalar =['ali','vali']    
baholar =bahola(talabalar[:])
print(baholar)