# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 20:03:31 2021

@author: Admin
"""


# print("Yaqin do'stlaringiz ro'yxatni tuzamiz")
# ismlar = []
# n= 1
# while True:
#     savol =f"{n} - do'stingizni ismini kiriting"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi (ha/yo'q)\n")
#     n+=1
#     if takrorlash != 'ha':
#         break
# print("do'stlaringiz ro'yxati")
# for ism in ismlar :
#     print(ism.title())
#for ism,yosh,    



# dostlar = {}
# ishora = True
# while ishora:
#     ism =input("Do'stingiz ismini kiriting")
#     yosh = input(f"{ism.title()}ning yoshini kiriting")
#     dostlar[ism]= int(yosh)
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob =='yo\'q':
#         ishora = False
        
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")      







# cars=['lacetti','lacetti','lacetti','lacetti']  
# while 'lacetti' in cars:
#     cars.remove('lacetti')
# print(cars)    







talabalar =['olim','vali','ali']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] =  int(baho)
    