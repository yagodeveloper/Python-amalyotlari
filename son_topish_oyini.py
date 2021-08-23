# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:58:34 2021

@author: Admin
"""

import random
def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"men 1 dan {x} gacha o'yladim topa olasizmi? ")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin= int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son kattaroq")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son kichkinaroq")
        else:
            break
        return taxminlar
    print(f"{taxminlar} ta taxmin bilan topdingiz")
        
print(sontop())
def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar +=1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob=print(f"siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
              f"men o'lagan son bundan kattaroq (+),yoki kichikroq (-)".lower())
        if javob=="-":
            yuqori = taxmin-1
        elif javob=="+":
            yuqori = taxmin+1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim")
    return taxminlar
  
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print("yutdim")
        elif taxminlar_user<taxminlar_pc:
            print("siz yutdingiz")
        else:
            print("durrang")
        yana = int(input("yana o'ynaysizmi ha(1) yo'q(0)"))
play()













      