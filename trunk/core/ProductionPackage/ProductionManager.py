# -*- coding: latin-1 -*-

'''
Created on 25 févr. 2011

@author: goungy
'''

from core.ProductionPackage.ProductionTimerFactory import ProductionTimerFactory
from core.ProductionPackage.ProductionObjectPackage.ProductionObjectFactory import ProductionObjectFactory
from core.ProductionPackage.ProductionRuleFactory import ProductionRuleFactory
import math

        

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
        self.production_rule_factory = ProductionRuleFactory(resource_manager, self.productionTimerFactory)
        self.last_starting_index = 0

    def update(self, iteration, production_update_frequency = 25, minimum_production_chunk = 50):
        if not iteration % production_update_frequency:
            self.wait_for_next_iteration_update = False
        if not self.wait_for_next_iteration_update:
            nb_prod_objects = self.get_nb_production_objects()
            portion_to_update = (math.ceil(float(nb_prod_objects) / float(production_update_frequency)))
            #print("Portion to update = max("+str(math.ceil(float(nb_prod_objects) / float(25)))+","+str(minimum_production_chunk))
            start_production_index = self.last_starting_index
            end_production_index = min(nb_prod_objects, start_production_index + portion_to_update)
            #print("iteration "+str(iteration)+" producing for objects "+str(start_production_index)+" to "+str(end_production_index)+" over "+str(nb_prod_objects))
            for po in self.get_all_production_objects()[start_production_index: end_production_index]:
                po.update(iteration)
            self.last_starting_index = end_production_index
            if end_production_index == nb_prod_objects:
                if iteration % production_update_frequency:
                    #print("Finished before the end")
                    self.wait_for_next_iteration_update = True
                self.last_starting_index = 0
            pass
        else:
            #print("Iteration "+str(iteration)+" waiting to produce")
            pass

    def get_all_production_objects(self):
        return self.productionObjectFactory.get_all_production_objects()
    
    def get_nb_production_objects(self):
        return len(self.get_all_production_objects())
      
    def start_global_production(self):
        self.productionTimerFactory.start_global_production()

    def is_global_production_stalled(self):
        return self.productionTimerFactory.is_global_production_stalled()

    def create_small_planet(self, stock_manager):
        self.productionObjectFactory.create_small_planet(stock_manager, self.production_rule_factory, self.productionTimerFactory)
        
    def create_small_factory(self, resource, stock_manager):
        self.productionObjectFactory.create_small_factory(resource, stock_manager, self.production_rule_factory, self.productionTimerFactory)
    
    def terminate_timers(self):
        self.productionTimerFactory.terminate_timers()
                   
    def __str__(self):
        return "Production Manager : \n" + "\n".join(str(i) for i in self.production_objects_list)