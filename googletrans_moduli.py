# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:06:47 2021

@author: Admin
"""

from googletrans import Translator
tarjimon = Translator()
matn_uz = "Python dunyodagi eng mashhur dasturlash tili"

# tarjima = tarjimon.translate(matn_uz)

# #original matn
# # print(tarjimon.origin)


# #tarjima

# print(tarjima.text)
# #original matn tili
# print(tarjima.src)

tarjima_ru = tarjimon.translate(matn_uz, dest="ru")
print(tarjima_ru.text)