# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 00:31:39 2021

@author: Admin
"""

# def toliq_ism_yasa(ism,familiya):
#    "" "toliq ism qaytaradigan funksiya"""
#    toliq_ism=f"{ism} {familiya}"
#    return toliq_ism
# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('rahim', 'hakimov')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}" )


# def toliq_ism_yasa(ism,familiya,otasining_ismi):
#     if otasining_ismi:
#         toliq_ism =f"{ism} {familiya} {otasining_ismi}"
#     elif ism:
#         toliq_ism =f"{ism} {familiya} {otasining_ismi}"
#     elif familiya:
#         toliq_ism =f"{ism} {familiya} {otasining_ismi}"
#     else:
#         toliq_ism = f"ism ham, familiya ham, otasining ismi ham aniqlanmadi"
#     return toliq_ism.title()    
# men = toliq_ism_yasa(ism=input("ismingizni kiriting"),
#                      familiya=input("familiyangizni kiriting"),
#                      otasining_ismi=input("otangizni ismini kiriting"))
# print(men)        


def oraliq(min,max,qadam):
    sonlar = []
    while min<max:
        sonlar.append(min)
        if qadam>1:
            min=min+qadam
        else:
            min+=1
    return sonlar
print(oraliq(2, 90,-8))

    