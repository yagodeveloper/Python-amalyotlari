# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:19:42 2021

@author: Admin
"""

import unittest
from cars import Car


class CarTest(unittest.TestCase):
    """Car klassini tekshirish ucun test"""
    def setUp(self):
        make = "GM"
        model = "Malibu"
        year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1=Car(make,model,year)
        self.avto2=Car(make,model,price=self.price)
    def test_create(self):
        #qiymatlar boryoki yo'q ekanligini tekshiruvchi metod
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        
        #qiymat mavjud emasligini tekshiruvchi metod
        
        self.assertIsNone(self.avto1.price)
        #qiymat mavjud ekanligini tekshiruvchi qiymat
        
        self().assertEqual(0,self.avto1.get_km())
        
        
        
        #avto2 narhini tekshiramiz
        self().assertEqual(0,self.avto2.price)
    def test_set_price(self):
        new_price = 45000
        self.test_price(new_price)
        self.assertEqual(new_price,self.avto2.price)
        
        
    def test_add_km(self):
        self.avto1.add_km(self.km)
        self.assertEqual(self.km,self.avto1.get_km)
        
        
        # new_km=-50000
        # try:
        #     self.avto1.add_km(new_km)
        # except ValueError as error:
        #     self.assertEqual(type(error),ValueError)


unittest.main()
            
        