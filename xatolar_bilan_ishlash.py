# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 22:46:52 2021

@author: Admin
"""
#ValueError xatoliklar 
# yosh = input("Yoshingizni kiriting:")
# yil =2021
# try:
#     yosh = int(yosh)
# except:
#     print("Siz butun son kiritmadingiz")
# else:
#     print(f"Siz {yil-yosh} yilda tug'ulgansiz")
    
    
    
# #ZeroDivisionError  xatoliklar
# x,y=5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")
    
    
#IndexError
# mevalar = ['olma','uzum','nok',"o'rik"]
# try:
#     print(f"{mevalar [4]}")
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")



#KeyError xatoliklar


# user = {"username":"Samandar",
#         "status":"admin",
#         "email":"yagocoder@gmail.com",
#         "phone":"+998 ** *** ** **"
#         }
# key ="tel"

# try:
#     print(f"Foydalanuvchi {user[key]}")
# except KeyError:
#     print("Bunday kalit so'z mavjud emas")

#FileNotFaundError


filename = 'data.txt'
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"{filename} mavjud emas")