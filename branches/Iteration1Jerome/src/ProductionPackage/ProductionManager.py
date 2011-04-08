# -*- coding: latin-1 -*-

'''
Created on 25 févr. 2011

@author: goungy
'''
from ProductionPackage.ProductionObject import ProductionObject
from ResourcesPackage.ProductionLine import ProductionLine

from ProductionPackage.ProductionTimerFactory import ProductionTimerFactory
from ProductionPackage.ProductionObjectFactory import ProductionObjectFactory

        

class ProductionManager(object):
    '''
    classdocs
    '''



    def __init__(self, resource_manager):
        '''
        Constructor
        '''
        self.productionTimerFactory = ProductionTimerFactory(resource_manager)
        self.productionObjectFactory = ProductionObjectFactory(resource_manager)     

    def get_all_production_objects(self):
        return self.productionObjectFactory.get_all_production_objects()
      
    def start_global_production(self):
        self.productionTimerFactory.start_global_production()

    def is_global_production_stalled(self):
        return self.productionTimerFactory.is_global_production_stalled()

    def create_small_planet(self, stock_manager):
        self.productionObjectFactory.create_small_planet(stock_manager, self.productionTimerFactory)
        
    def create_small_factory(self, resource, stock_manager):
        self.productionObjectFactory.create_small_factory(resource, stock_manager, self.productionTimerFactory)
    
    def terminate_timers(self):
        self.productionTimerFactory.terminate_timers()
                   
    def __str__(self):
        return "Production Manager : \n" + "\n".join(str(i) for i in self.production_objects_list)