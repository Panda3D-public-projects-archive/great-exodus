# -*- coding: latin-1 -*-

'''
Created on 25 févr. 2011

@author: goungy
'''
from ResourcesPackage.ResourcesManager import ResourcesManager
from ProductionPackage.ProductionObject import ProductionObject
from ResourcesPackage.StockManager import StockManager
from ProductionPackage.ProductionManager import ProductionManager

import time
class ProductionUseCase1(object):
    '''
    classdocs
    '''

    def __init__(self, nb_objects):
        '''
        Constructor
        '''
        resource_manager = ResourcesManager()
        self.stock_manager = StockManager(resource_manager)
        self.production_manager = ProductionManager(resource_manager) 
        # Creating production objects
        
        for i in range(nb_objects):
            self.production_manager.create_small_mineral_planet(self.stock_manager)
            self.production_manager.create_medium_mineral_planet(self.stock_manager)
            self.production_manager.create_large_mineral_planet(self.stock_manager)
            self.production_manager.create_small_wood_planet(self.stock_manager)
            self.production_manager.create_medium_wood_planet(self.stock_manager)
            self.production_manager.create_large_wood_planet(self.stock_manager)
            self.production_manager.create_small_silex_station(self.stock_manager)
            self.production_manager.create_medium_silex_station(self.stock_manager)
            self.production_manager.create_large_silex_station(self.stock_manager)        
        
        print "Launching test with " + str(9*nb_objects) + " objects"
        starting_time = time.time()
        self.production_manager.start_global_production()
        while (self.production_manager.is_global_production_stalled() == False):
            time.sleep(0.5)
        ending_time = time.time()
        print "Execution Time = " + str(ending_time-starting_time) + " s"
        