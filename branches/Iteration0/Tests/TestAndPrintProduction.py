'''
Created on 20 avr. 2011

@author: JD219546
'''
import unittest
from controller.Controller import Controller



class TestAndPrintController(unittest.TestCase):
    
    def __init__(self, nb_objects, iterations=1):
        self.controller = Controller()
        self.__create_production(nb_objects)
        self.controller.stock_manager.print_global_stock()
        print("####### PRODUCING #######")
        self.controller.run(iterations)
        self.controller.stock_manager.print_global_stock()

    def __create_production(self, nb_objects):
        prod_manager = self.controller.production_manager
        res_manager = self.controller.resource_manager
        stock_manager = self.controller.stock_manager
        for i in range(nb_objects):
            prod_manager.create_small_planet(stock_manager)
            for r in res_manager.resource_list:
                prod_manager.create_small_factory(r, stock_manager)

if __name__ == "__main__":
    tapc = TestAndPrintController(1)
    