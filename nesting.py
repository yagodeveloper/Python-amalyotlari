# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:49:27 2021

@author: Admin
"""

# car0 = {'model':'gentra',
#        'rang':'qizil',
#        'yil':2019,
#        'narh':13000,
#        'km':40000,
#        'karobka':'avtomat'
       
#        }
# car1 = {'model':'nexia 2',
#        'rang':'qizil',
#        'yil':2010,
#        'narh':5000,
#        'km':70000,
#        'karobka':'avtomat'
       
#        }
# car2 = {'model':'malibu',
#        'rang':'qora',
#        'yil':2015,
#        'narh':15000,
#        'km':40000,
#        'karobka':'avtomat'
       
#        }
# car3 = {'model':'orlando',
#        'rang':'qizil',
#        'yil':2013,
#        'narh':13000,
#        'km':40000,
#        'karobka':'avtomat'
       
#        }
# car = car0
# print(f"{car['model'].title()}",
#       f"{car['rang']} rang",
#       f"{car['yil']}, {car['narh']} $",
#       )
# car = car1
# print(f"{car['model'].title()}",
#       f"{car['rang']} rang",
#       f"{car['yil']}, {car['narh']} $",
#       )
# car = car2
# print(f"{car['model'].title()}",
#       f"{car['rang']} rang",
#       f"{car['yil']}, {car['narh']} $",
#       )
# car = car3
# print(f"{car['model'].title()}",
#       f"{car['rang']} rang",
#       f"{car['yil']}, {car['narh']} $",
 #     )

#onson yo'lda chiqarish


# cars = [car0,car1,car2,car3]
# for car in cars:
#     print(f"{car['model'].title()}",
#        f"{car['rang']} rang",
#        f"{car['yil']} yil, {car['narh']} $",
#       ) 


# malibus =[]
# for n in range(10):
#     new_car={'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':13000,
#         'km':40000,
#         'karobka':'avtomat'}
#     malibus.append(new_car)


# # for malibu in malibus:
# #     print(malibu)


# for malibu in malibus[0:1]:
#     malibu['model']='nexia'
    
# for malibu in malibus[1:3]:
#     malibu['model']='matiz'    

# for malibu in malibus:
#     print(malibu)
 





#lo'gat ichida ro'yxatlar


dasturchilar={
    'ali':['html','css','javascript'],
    'vali':['python','java']
    } 

for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi")
    for til in tillar:
        print(til.upper())