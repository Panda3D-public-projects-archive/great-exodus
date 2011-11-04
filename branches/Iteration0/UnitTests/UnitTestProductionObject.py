'''
Created on 8 avr. 2011

@author: JD219546
'''
import unittest
from UnitTests.CheckingProductionObject import CheckingProductionObject


class Test(unittest.TestCase):


    def testName(self):
        CheckingProductionObject(1000)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()