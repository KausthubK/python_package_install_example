#!/usr/bin/python3
"""
Module 2
"""

import unittest

from kkpkgs.kkpkg1 import mod2 as sut

class TestMod2(unittest.TestCase):
    def setUp(self) -> None:
        self.manual_test = False

    def test_fn1(self):
        sut.fn1()
        self.assertTrue(True)
    
    def test_fn2(self):
        sut.fn2()
        self.assertTrue(True)
        
        

if __name__ == '__main__':
    unittest.main()