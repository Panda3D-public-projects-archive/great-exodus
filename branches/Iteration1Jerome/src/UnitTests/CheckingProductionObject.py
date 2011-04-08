'''
Created on 8 avr. 2011

@author: JD219546
'''
from ResourcesPackage.ResourcesManager import ResourcesManager
from ResourcesPackage.StockManager import StockManager
from UnitTests.CheckingStockManager import CheckingStockManager
from ProductionPackage.ProductionManager import ProductionManager

class CheckingProductionObject(object):
    '''
    classdocs
    '''


    def __init__(self, nb_objects):
        '''
        Constructor
        '''

        resource_manager = ResourcesManager()
        self.stock_manager = StockManager(resource_manager,1)
        self.production_manager = ProductionManager(resource_manager)
        # Creating production objects
        obj_count = 0
        for i in range(nb_objects):
            self.production_manager.create_small_planet(self.stock_manager)
            obj_count += 1
            for r in resource_manager.resource_list:
                self.production_manager.create_small_factory(r, self.stock_manager)
                obj_count += 1
                
        print "Launching test with " + str(obj_count) + " objects"
        for prodObj in self.production_manager.get_all_production_objects():
            self.test(prodObj)
                
        
    def test_empty_starting_stock(self, prodObj):
        obj_stock = prodObj.stock
        for i in obj_stock.stock_dict.values():
            i[0] = 0
        i = 0
        for p in prodObj.getProduced_resources():
            prodObj.evolve_stock(p)
            resourceNeeded = p.input_resource_lines
            if resourceNeeded and obj_stock.stock_dict[p][0] > 0:
                raise Exception("Object "+str(i)+" with empty stock produced something!!!")
            i += 1
        
        
    def test_full_starting_stock(self, prodObj):
        obj_stock = prodObj.stock
        for i in obj_stock.stock_dict.values():
            i[0] = i[1]
        i = 0
        for p in prodObj.getProduced_resources():
            prodObj.evolve_stock(p)
            if obj_stock.get_stock_for_resource(p) <= 0:
                raise Exception("Object "+str(i)+" with full entry stock produced nothing!!!")
            i += 1
        
    
    def test(self, prodObj):
        self.test_empty_starting_stock(prodObj)
        self.test_full_starting_stock(prodObj)
        