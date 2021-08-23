# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 19:46:18 2021

@author: Admin
"""
#ANDOZA OLISH INTERNET MANZILI iHateRegex.io
import re
from words_list import words

word1 = "tomir"
word2 = "temur"
word3 = "tulpor"

andoza = "^t...r$"
  

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

matches = []
for word in words:
    if re.match(andoza, word):
        matches.append(word)


print(matches)