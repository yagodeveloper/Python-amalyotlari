# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 01:29:59 2021

@author: Admin
"""

dasturlash_tillari =['java','Python','C++','JavaScript','C']#matnli ro'yxatlar

urganish_pullari =[20000,30000,40000]#sonli ro'yxatlar

sonlar=['bir','ikki',3,4,5,]#aralash ro'yxatlar

bosh=[]#bo'sh ro'yxat

#print("Birinchi dasturlash tili",dasturlash_tillari[0])
#print("Birinchi dasturlash tili",dasturlash_tillari[1])

print("Birinchi dasturlash tili",dasturlash_tillari[0].upper())
print("Birinchi dasturlash tili",dasturlash_tillari[0].title())

print(urganish_pullari[0]+urganish_pullari[-1])

#elementni o'zgartirish


urganish_pullari[0]=21000
urganish_pullari[1]=25000

print(urganish_pullari[0]+urganish_pullari[1])

#ro'yxatga yana qo'shimcha elementlar qo'shuvchi metodlar

dasturlash_tillari.append('CSS')#ro'yxatni oxiriga yangi malumat qo'shadigan metod

dasturlash_tillari.insert(1, 'HTML') #ro'yxatni xohlagan joyiga malumot qo'shadigan metod

#ro'yxatdagi elementni o'chiruvchi metodlar

#1-usul
del dasturlash_tillari[0]#index qiymati bilan o'chirish yani raqami bilan

#2-usul
dasturlash_tillari.remove("C")#berilgan malumotlari bilan o'chirish
#birinchi uchragan metodni o'chiradi

#ro'yxatni ichidan biror elementni sug'rib oluvchi metod
raqam=urganish_pullari.pop(1)

# pop metodiga index berilmasa u holda u oxirgi elementni qirqib oldi

