'''
Created on 8 avr. 2011

@author: JD219546
'''
from core.ProductionPackage.ProductionObject import ProductionObject

class ProductionObjectFactory(object):
    '''
    classdocs
    '''


    def __init__(self, resource_manager):
        '''
        Constructor
        '''
        self.production_objects = []
        
        self.small_planet_production = [resource_manager.ore, resource_manager.ice]

    def create_small_planet(self, stock_manager, productionTimerFactory):
        po = self.create_production_object( stock_manager.create_small_planet_stock(), self.small_planet_production, productionTimerFactory)
        productionTimerFactory.add_small_production_object(po)
        self.add_production_object_to_list(po)
        
    def create_small_factory(self, resource, stock_manager, productionTimerFactory):
        po = self.create_production_object( stock_manager.create_small_factory_stock(resource), [resource, ], productionTimerFactory)
        productionTimerFactory.add_small_production_object(po)
        self.add_production_object_to_list(po)
                
    def add_production_object_to_list(self,po):
        self.production_objects.append(po)
        
    def create_production_object(self, stock, production_lines, productionTimerFactory):
        po = ProductionObject(stock, production_lines, productionTimerFactory)
        return po  
    
    def get_all_production_objects(self):
        return self.production_objects