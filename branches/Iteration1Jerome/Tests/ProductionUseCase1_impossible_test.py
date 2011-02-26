# -*- coding: latin-1 -*-
'''
Created on 26 févr. 2011

@author: goungy
'''
import unittest
from Tests.ProductionUseCase1 import ProductionUseCase1


class Test(unittest.TestCase):

#start =0810.44 s 


#end   = 844.53
#time  = 34.09
    def testName(self):
        ProductionUseCase1(100000)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()