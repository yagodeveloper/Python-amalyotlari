# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:52:56 2021

@author: Admin
"""

class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
    def tanishtir(self):
        return f"Ismim {self.ism} familiyam {self.familiya} tug'ulgan yilim {self.tyil}"
    def get_name (self):
        return self.ism
    def get_age(self,yil):
        return yil - self.tyil
    def get_info(self):
        return f"Ismim {self.ism} familiyam {self.familiya} yoshim {self.yil} bosqichim {self.bosqich}"

#talaba1 = Talaba(input("ismni kiriting"), input("familiyani kiriting"),int( input("tug'lgan yilni kiriting"))) 
#print(talaba1) 
  

class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    def add_students(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni +=1
    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]
matematika = Fan('oliy matematika')
talaba1 = Talaba("ali", "valiyev", 2000)
matematika.add_students(talaba1)    
#klasni ichidagi obyektlarni ko'rish uchun mo'ljallangan metod
#dir(klasnomi)    