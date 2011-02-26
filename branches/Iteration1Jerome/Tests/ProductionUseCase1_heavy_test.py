# -*- coding: latin-1 -*-
'''
Created on 26 févr. 2011

@author: goungy
'''
import unittest
from Tests.ProductionUseCase1 import ProductionUseCase1


class Test(unittest.TestCase):

    def testName(self):
        ProductionUseCase1(1000)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()