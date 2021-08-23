# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:49:23 2021

@author: Admin
"""

# def salom_ber():
#     """salom beruvchi funksiya"""
#     print("assalomu alaykum")
# salom_ber()   


# def salom_ber(ism):
#     """salom beruvchi funksiya"""
#     print(f"salom {ism.title()}")
# salom_ber('hasan')  


#funksiya haqidagi malumotni olish

#print(funksiya nomi.__doc__)



def toliq_ism(ism,familiya):
    """ism va familiya chiqaradigan funksiya"""
    print(f"foydalanuvchi ismi: {ism.title()}\n",
        f"foydalanuvchi familiyasi: {familiya.title()}"
          )
toliq_ism(ism='hasan',familiya= 'husanov')    