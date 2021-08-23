# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 02:21:10 2021

@author: Admin
"""

class Car:
    """Avtomabil klassi"""
    num_avto = 0
    def __init__(self, make,model,yil,km=0,price=None):
        """AVTOMOBIL XUSUSIYATLARI"""
        self.make = make
        self.model = model
        self.yil = yil
        self.__km = km
        self.price =price
        
        
    def set_price(self,price):
        self.price = price
        
    def add_km(self,km):
        """Mashina kilometriga yana km qo'shish"""
        if km>=0:
            self.__km +=km
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas")
            
            
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()} "
        info+=f"{self.yil} - yil,{self.__km}km yurgan"
        if self.price:
            info+=f"Narhi: {self.price}"
        return info
    def get_km(self):
        return self.__km