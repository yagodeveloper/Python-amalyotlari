# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:37:27 2021

@author: Admin
"""

class Shaxs:
    """Shaxslar haqida ma'lumat"""
    def __init__(self, ism , familiya, pasport , tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.pasport = pasport
        self.tyil = tyil
        
    def get_info(self):
        """shaxs haqida ma'lumot """
        info = f"{self.ism} {self.familiya}. "
        info += f"Pasport:{self.pasport}, {self.tyil} - yil"
        return info
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Talaba(Shaxs):
    """talaba klasi"""
    def __init__(self, ism, familiya, pasport, tyil,idraqam,manzil):
        """talabani xususiyatlari"""
        super().__init__(ism, familiya, pasport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        
    def get_id(self):
        """shaxsni idiraqamini qaytarish """
        return self.idraqam
    def get_bosqich(self):
        """talabani o'qish bosqichi """
        return self.bosqich
    def get_info(self):
        """shaxs haqida ma'lumot """
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich ID raqami: {self.idraqam} "
        return info
class Manzil:
    """Manzil saqlovchi klass"""
    def __init__(self, uy,kocha,tuman,viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
    def get_manzil(self):
        """ manzilni ko'rish """
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} kochasi, {self.uy} - uy"
        return manzil
talba_man = Manzil(21, "olmazor", "oqdaryo", "samarqand")    
talaba1 = Talaba("ali", "valiyev", "kl6070", 2001, "11111", talba_man) 
talaba1.manzil.get_manzil()   