# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 01:19:11 2021

@author: Admin
"""

from uuid import uuid4
class Avto:
    """Avtomabil klassi"""
    num_avto = 0
    def __init__(self, make,model,rang,yil,narh,km=0):
        """AVTOMOBIL XUSUSIYATLARI"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.num_avto +=1

    def __str__(self):
        return f"{self.make} {self.model}"
    
    
    def __repr__(self):
        return f"{self.make} {self.model}"
    
    def __eq__(self,y):
        return self.narh ==y.narh
    def __lt__(self,y):
        return self.narh <y.narh
    def __le__(self,y):
        return self.narh <=y.narh
class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
        
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    
    def __setitem__(self,index,qiymat):
         self.avtolar[index]=qiymat
         
    def __call__(self,*qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
        
    def __add__(self,boshqa_salon):
        yangisalon = AvtoSalon(f"{self.name} {boshqa_salon.name}")
        yangisalon.avtolar = self.avtolar + boshqa_salon.avtolar
        return yangisalon
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("avto qo'shing")
                
    
salon1 = AvtoSalon("MaxAvto")
salon2 = AvtoSalon("MinAvto")

avto1 = Avto("gm", "lacetti", "oq", 2000, 7000)
avto2 = Avto("gm", "lacetti", "oq", 2000, 8000) 
salon1.add_avto(avto1,avto2)


avto3 = Avto("gm", "lacetti", "oq", 2000, 8000)
avto4 = Avto("gm", "lacetti", "oq", 2000, 8000)
salon2(avto3,avto4)