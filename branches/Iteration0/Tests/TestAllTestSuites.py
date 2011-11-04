'''
Created on 25 avr. 2011

@author: JD219546
'''
import unittest
from Tests.TestController import TestController
from Tests.TestProductionObject import TestProductionObject
from Tests.TestProductionRule import TestProductionRule


class Test(unittest.TestCase):


    def test_all_test_suites(self):
        test_objects = [TestController, TestProductionObject, TestProductionRule]
        test_suites = []
        for test_obj in test_objects:
            test_suites.append(test_obj.suite())
        for test_suite in test_suites:
            unittest.TextTestRunner(verbosity=2,buffer=True).run(test_suite)
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_all_test_suites']
    unittest.main()