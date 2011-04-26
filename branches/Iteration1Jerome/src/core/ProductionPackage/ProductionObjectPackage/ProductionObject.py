# -*- coding: latin-1 -*-

'''
Created on 25 févr. 2011

@author: goungy
'''
from core.ProductionPackage.ProductionObjectPackage.ProductionObjectStatusManager import ProductionObjectStatusManager
from core.ProductionPackage.ProductionObjectStatus import ProductionObjectStatus

class MissingItemToProduceInStockException(Exception):
    
    def __init__(self, resource):
        self.resource = resource
        
class MissingNeededResourceInStockException(Exception):
    
    def __init__(self, resource):
        self.resource = resource

class ProductionObject(object):
    '''
    classdocs
    '''


    def check_stocks_ok_for_item(self, item_to_produce):
        if not self.stock.has_resource(item_to_produce):
            raise Exception("Item to produce (" + str(item_to_produce.name) + ") does not exist in stock manager : " + str(self.stock))
        for needed_resource in item_to_produce.input_resource_dict.keys():
            if not self.stock.has_resource(needed_resource):
                raise Exception("Item to produce (" + str(item_to_produce.name) + ") needs (" + str(needed_resource.name) + ") which is not in stock manager : " + str(self.stock))
        pass


    def check_stocks_and_create_needed_resource_map_for_item(self, item_to_produce):
        self.check_stocks_ok_for_item(item_to_produce)
        self.production_status[item_to_produce] = 0

    def check_stocks_have_resources_needed_and_items_to_produce(self):
        for produced_resource in self.production_rule.getProduced_resources():
            try:
                if not self.stock.has_resource(produced_resource):
                    raise MissingItemToProduceInStockException(produced_resource)
            except MissingItemToProduceInStockException:
                print(produced_resource.name+" is not present in stocks and produced")
                exit(0)
                
            for prod_need in self.production_rule.getNeeded_resources(produced_resource):
                res_needed = prod_need.resource
                try:
                    if not self.stock.has_resource(res_needed):
                        raise MissingNeededResourceInStockException(res_needed)
                except MissingNeededResourceInStockException:
                    print(res_needed.name+" is not present in stocks and needed for production")
                    exit(0)

    def __init__(self, stock, production_rule, production_timer_factory, iteration = 0):
        '''
        Constructor
        '''
        self.stock = stock
        self.production_rule = production_rule
        self.iteration = iteration
        self.production_object_status = ProductionObjectStatus(iteration)
        #self.production_object_status_manager.create_production_status(production_rule, production_timer_factory, iteration)
        #self.production_lines = production_lines
        self.check_stocks_have_resources_needed_and_items_to_produce()

    def update(self, iteration):
        enough_to_produce = self.production_rule.enough_to_produce(self.stock)
        enough_stock_room = self.production_rule.enough_stock_room(self.stock)
        #print("State before " + str(self.production_object_status.production_state))
        self.production_object_status.evolve_state(self,enough_to_produce,enough_stock_room, iteration)
        #print("State after " + str(self.production_object_status.production_state))
        self.production_object_status.produce(self)
        pass
    
    def produce(self):
        for item_to_produce in self.production_rule.getProduced_resources():
            production_line = self.production_rule.getProduction_line(item_to_produce)
            quantity_to_produce = production_line.quantity_to_produce
            #first: consuming products
            for prod_need in production_line.production_need_list:
                needed_quantity = quantity_to_produce * prod_need.quantity
                needed_res = prod_need.resource
                self.stock.decrease_resource(needed_res, needed_quantity)
            self.stock.increase_resource(item_to_produce, quantity_to_produce)
        pass
       
    def getProduced_resources(self):
        return self.production_rule.getProduced_resources()
        
    def getNeeded_resources(self, produced_resource):
        return self.production_rule.getNeeded_resources(produced_resource)
        
    def __str__(self):
        return "(ProductionObject)\n" + str(self.stock) + "\n(Production)" + "\n(Production)".join(str(i) for i in self.production_lines)