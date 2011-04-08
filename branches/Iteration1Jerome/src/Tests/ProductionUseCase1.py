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
from UnitTests.CheckingStockManager import CheckingStockManager
class ProductionUseCase1(object):
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
        checkingStockManager = CheckingStockManager(self.stock_manager) 
        # Creating production objects
        obj_count = 0
        for i in range(nb_objects):
            self.production_manager.create_small_planet(self.stock_manager)
            obj_count += 1
            for r in resource_manager.resource_list:
                self.production_manager.create_small_factory(r, self.stock_manager)
                obj_count += 1
        print ("")
        print ("")
        print ("Initial stock")
        print ("")
        #nb_stocks = len(self.stock_manager.get_all_stocks())
        #print( "Nb stocks =",nb_stocks)
        checkingStockManager.test()
        if (obj_count < 30): self.stock_manager.print_global_stock()
        
        print ("")
        print ("Launching test with " + str(obj_count) + " objects")
        starting_time = time.time()
        self.production_manager.start_global_production()
        while (self.production_manager.is_global_production_stalled() == False):
            time.sleep(0.5)
        self.production_manager.terminate_timers()
        ending_time = time.time()
        print ("")
        print ("")
        print ("Final stock")
        print ("")
        checkingStockManager.test()
        if (obj_count < 30): self.stock_manager.print_global_stock()
        print ("")
        print ("SUCCESSFUL execution of the Use Case")
        print ("Execution Time = " + str(ending_time-starting_time) + " s")
        