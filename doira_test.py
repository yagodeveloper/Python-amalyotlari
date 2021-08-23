# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:55:10 2021

@author: Admin
"""

import unittest
from doira import getArea,getPeremetr


class DoiraTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5), 78.53975)
        self.assertAlmostEqual(getArea(5), 314.159)
        
unittest.main()        