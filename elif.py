# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 13:27:00 2021

@author: Admin
"""

#yosh= int(input('yoshingiz nechada'))
#if yosh<5:
#    print('kirish bepul')
#elif yosh<12:
 #   print('kirish 5000 so\'m')
#elif yosh<18:
  #  print('kirish 8000 so\'m')    
#else:
   # print('kirish 10000 so\'m')    





#yosh= int(input('yoshingiz nechada'))
#if yosh<5:
 #   narh = 'bepul'
#elif yosh<12:
#    narh = 5000
#elif yosh<18:
 #   narh= 8000    
#else:
  #  narh = 10000
#print(f'sizga kirish narhi {narh} so\'m')


#kun = input('bugun qaysi kun')
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
 #   print('dam olish kun')
#else:
#    print('bugun ish kuni')
    
    
    
    
    
    
#kun = input('bugun qaysi kun')
#harorat = float(input('harorat necha gradus'))


#if kun.lower()=='shanba' and harorat >= 30:
 #   print('cho\'milishga ketdik')
#elif kun.lower()=='shanba' and harorat < 30:
 #   print('bugun uyda dam olamiz')
  
narh = 15000
choy= input('choy olasizmi')
salat= input('salat olasizmi')
non =input('non olasizmi')
kampot = input('kompot okasizmi')
assorti = input('assorrti olasizmi ')


if choy.lower()==' ha':
    print('mijoz choy oldi')
    narh=narh+3000
    
else:
    print('mijoz choy olmadi')

if salat.lower()=='ha':
    print('mijoz salat oldi')
    narh=narh+5000
else:
    print('mijoz salat olmadi')
if non.lower()=='ha':
    print('mijoz non oldi')
    narh=narh+2000
else:
    print('mijoz non olmadi')
if kampot.lower()=='ha':
    print('mijoz kampot oldi')
    narh=narh+5000
else:
    print('mijoz kampot olmadi')
if assorti.lower()=='ha':
    print('mijoz assorti oldi')
    narh=narh+6000
else:
    print('mijoz assorti olmadi')  
print(narh)   
 
    