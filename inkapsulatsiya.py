# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 23:00:27 2021

@author: Admin
"""

from uuid import uuid4
class Avto:
    """Avtomabil klassi"""
    def __init__(self, make,model,rang,yil,narh,km=0):
        """AVTOMOBIL XUSUSIYATLARI"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    def add_km(self,km):
        """Mashinaning kilometriga yana kilometr qo'shuvchi funksiya"""
        if km>=0:
            self.__km += km
        else:
            print("mashinananing kilometrini kamaytirib bo'lmaydi")