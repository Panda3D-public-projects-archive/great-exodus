'''
Created on 20 avr. 2011

@author: JD219546
'''
import unittest
from controller.Controller import Controller



class TestController(unittest.TestCase):

    def __create_production(self, nb_objects):
        prod_manager = self.controller.production_manager
        res_manager = self.controller.resource_manager
        stock_manager = self.controller.stock_manager
        for i in range(nb_objects):
            prod_manager.create_small_planet(stock_manager)
            for r in res_manager.resource_list:
                prod_manager.create_small_factory(r, stock_manager)
                
    def __create_production_test_and_run(self, nb_objects, iterations=27):
        self.__create_production(nb_objects)
        self.controller.run(iterations)
        self.__control_time()

    def __control_time(self):
        start = self.controller.controller_timer.overall_start
        end = self.controller.controller_timer.current_time
        elapsed_time = end - start
        expected_time = self.controller.nb_iterations * self.controller.controller_timer.time_tick
        time_difference = abs(elapsed_time - expected_time)
        relative_difference = float(time_difference) / float(expected_time)
        if relative_difference > 0.05:
            raise Exception("Time difference too large:"+str(elapsed_time)+" and " + str(expected_time))

    def setUp(self):
        self.controller = Controller()
        pass


    def tearDown(self):
        pass


    def test_0_empty_run(self):
        self.controller.run()
        pass

    def test_1_small_production_run(self):
        self.__create_production_test_and_run(1)
        pass
    
    def test_2_medium_production_run(self):
        self.__create_production_test_and_run(10)
        pass
    
    def test_3_large_production_run(self):
        self.__create_production_test_and_run(100)
        pass
    
    def test_4_very_large_production_run(self):
        self.__create_production_test_and_run(1000)
        pass

    @staticmethod
    def suite():
        suite = unittest.TestSuite()    
        suite.addTest(unittest.makeSuite(TestController))
        return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1,buffer=True).run(TestController.suite())
    #import sys;sys.argv = ['', 'Test.testController']
    #unittest.main()