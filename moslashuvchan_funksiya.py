# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 01:54:02 2021

@author: Admin
"""

# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(1.9,2,6))


#kalit so'zli funksiya


def avto_info(kompaniya,model,**malumotlar):
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
avto1 = avto_info("gm",'malibu',rang='qora')
print(avto1)
    