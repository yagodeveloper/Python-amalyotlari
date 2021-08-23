# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:21:40 2021

@author: Admin
"""

def get_full_name(ism,familiya,otasi=''):
    if otasi:
        return f"{ism} {familiya} {otasi}".title()
    else:
        return f"{ism} {familiya}".title()