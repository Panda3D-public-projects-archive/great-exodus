# -*- coding:utf-8 -*-
"""
Created on 21 avr. 2011

@author: JD219546
"""

class ProductionObjectStatusFactory:
    
    def __init__(self):
        self.production_object_status_map = []
        pass
    
    def create_production_status(self, resource_to_produce, production_timer_factory, iteration):
        if resource_to_produce not in self.production_object_status_map.keys():
            production_time = production_timer_factory.get_production_timer(resource_to_produce)
            prod_status = ProductionObjectStatus(production_time, iteration)
            self.add_production_status_to_list(prod_status)
        else:
            raise Exception("Item already set to be produced in ProductionObjectStatusFactory")
        
        