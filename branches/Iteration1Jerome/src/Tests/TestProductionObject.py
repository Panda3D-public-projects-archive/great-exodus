'''
Created on 8 avr. 2011

@author: JD219546
'''
import unittest

from multiprocessing import Pool
from controller.Controller import Controller
from multiprocessing.process import Process



def static_test_empty_starting_stock( prodObj):
    obj_stock = prodObj.stock
    for i in obj_stock.stock_dict.values():
        i.quantity = 0
    i = 0
    for p in prodObj.getProduced_resources():
        prodObj.update(0)#evolve_stock(p)
        resourceNeeded = prodObj.getNeeded_resources(p)
        if resourceNeeded and obj_stock.stock_dict[p].quantity > 0:
            raise Exception("Object "+str(i)+" with empty stock produced something!!!")
        i += 1
    
def static_put_zero_in_production_and_full_needed_in_stock(prodObj):
    obj_stock = prodObj.stock
    for i in obj_stock.stock_dict.values():
        i.quantity = i.max_stock
    for p in prodObj.getProduced_resources():
        obj_stock.stock_dict[p].quantity = 0   
    
def static_test_full_starting_stock( prodObj):
    obj_stock = prodObj.stock
    i = 0
    for p in prodObj.getProduced_resources():
        prodObj.update(0)
        if obj_stock.get_stock_for_resource(p) <= 0:
            raise Exception("Object "+str(i)+" with full entry stock produced nothing!!!")
        #print ("Object produced "+str(obj_stock.get_stock_for_resource(p)) +" "+p.name)
        i += 1


def multiply_by_two(list):
    for elt in list:
        elt *= 2

class TestProductionObject(unittest.TestCase):
    '''
    classdocs
    '''

    def __create_production(self, nb_objects):
        prod_manager = self.controller.production_manager
        res_manager = self.controller.resource_manager
        stock_manager = self.controller.stock_manager
        for i in range(nb_objects):
            prod_manager.create_small_planet(stock_manager)
            for r in res_manager.resource_list:
                prod_manager.create_small_factory(r, stock_manager)
        #print("Testing "+str(prod_manager.get_nb_production_objects())+" production objects")

    def setUp(self):
        '''
        Constructor
        '''
        self.controller = Controller()
        self.nb_procs_for_tests = 4
        self.nb_objects_for_tests = 1
        self.process_pool = Pool(self.nb_procs_for_tests)
        self.__create_production(self.nb_objects_for_tests)             
        
    def test_full_starting_stock(self):
        #self.process_pool.map_async(static_test_empty_starting_stock,self.controller.production_manager.get_all_production_objects())
        
        for prodObj in self.controller.production_manager.get_all_production_objects():
            static_put_zero_in_production_and_full_needed_in_stock(prodObj)
        #self.controller.stock_manager.print_global_stock()
        for prodObj in self.controller.production_manager.get_all_production_objects():
        #    self.process_pool.apply_async(static_test_empty_starting_stock,prodObj)#self.__test_empty_starting_stock(prodObj)
            static_test_full_starting_stock(prodObj)
        #self.controller.stock_manager.print_global_stock()
        #raise Exception("To force display")
        #self.process_pool.close()
        #self.process_pool.join()
            
    def test_empty_starting_stock(self):

        #self.process_pool.map_async(static_test_empty_starting_stock,self.controller.production_manager.get_all_production_objects())
        for prodObj in self.controller.production_manager.get_all_production_objects():
        #    self.process_pool.apply_async(static_test_empty_starting_stock,prodObj)#self.__test_empty_starting_stock(prodObj)
            static_test_empty_starting_stock(prodObj)
        #self.process_pool.close()
        #self.process_pool.join()       

    @staticmethod  
    def suite():
        suite = unittest.TestSuite()    
        suite.addTest(unittest.makeSuite(TestProductionObject))
        return suite        
    
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2,buffer=True).run(TestProductionObject.suite())
        