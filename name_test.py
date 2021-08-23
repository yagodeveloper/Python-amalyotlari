# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:25:15 2021

@author: Admin
"""

import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name('alijon', 'valiyev')
        self.assertEqual(name, 'Alijon Valiyev')
    def test_otasi_ism(self):
        name = get_full_name('alijon', 'valiyev','olimovich')
        self.assertEqual(name, 'Alijon Olimovich Valiyev')

unittest.main()