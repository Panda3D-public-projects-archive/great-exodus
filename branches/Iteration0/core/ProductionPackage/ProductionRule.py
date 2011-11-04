# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''
from core.ProductionPackage.ProductionLine import ProductionLine

class MultipleSameItemToProduceException(Exception):
    
    def __init__(self, resource):
        self.resource = resource
            

class ProducedNeededDependencyException(Exception):
    
    def __init__(self, resource):
        self.resource = resource

class ProductionRule(object):
    '''
    classdocs
    '''


    def check_produced_needed_dependency(self, production_need_list):
        for item_to_produce in self.production_map.keys():
            for production_need in production_need_list:
                if production_need:
                    print(production_need)
                    if item_to_produce == production_need.resource:
                        print(item_to_produce.name + " is a produced item but also used for another resource")
                        print("This is currently unsupported!")
                        raise ProducedNeededDependencyException(item_to_produce)
            
    def check_lists_length(self, resources_needed, items_to_produce, production_times, quantities):
        all_lengths_ok = len(resources_needed) == len(items_to_produce) and len(items_to_produce) == len(production_times) and len(production_times) == len(quantities)
        if not all_lengths_ok:
            print("Lengths:")
            print("resources_needed: " + str(len(resources_needed)))
            print(resources_needed)
            print("items_to_produce: " + str(len(items_to_produce)))
            for item in items_to_produce:
                print("item = " + item.name)
            print("production_times: " + str(len(production_times)))
            print("quantities: " + str(len(quantities)))
            raise Exception("Error in items length in ProductionRule:")

    def resource_in_multiple_production(self, resource):
        for prod_line in self.production_map.values():
            for prod_need in prod_line.production_need_list:
                if resource == prod_need.resource:
                    return True
        return False

    def check_and_add_production_line(self, item_to_produce, production_line):
        
        #testing if item is not already being produced
        if item_to_produce in self.production_map.keys():
            raise MultipleSameItemToProduceException(item_to_produce)
        
        
        for production_need in production_line.production_need_list:
            actual_needed_resource = production_need.resource
            #checking if resources needed is not needed for another production line
            if self.resource_in_multiple_production(actual_needed_resource):
                self.careful_needed_resources.add(actual_needed_resource)
            #checking if resources needed to produce new item is not a product from previous production line
            if actual_needed_resource in self.production_map.keys():
                raise ProducedNeededDependencyException(actual_needed_resource)

        for tmp_prod_line in self.production_map.values():
            for prod_need in tmp_prod_line.production_need_list:
                #print("Testing ["+item_to_produce+"] and ["+prod_need.resource+"]")
                if item_to_produce == prod_need.resource:
                    raise ProducedNeededDependencyException(item_to_produce)
                
        self.production_map[item_to_produce] = production_line
        pass

    def __init__(self, resources_needed = [], items_to_produce = [], production_times = [], quantities = []):
        '''
        Constructor
        '''
        self.check_lists_length(resources_needed, items_to_produce, production_times, quantities)
        self.production_map = {}
        self.careful_needed_resources = set()
        
        len_list = len(resources_needed)
        for i in range(len_list):
            current_item_to_produce = items_to_produce[i]
            current_production_line = ProductionLine(resources_needed[i], production_times[i], quantities[i])
            self.check_and_add_production_line(current_item_to_produce, current_production_line)
        #raise Exception("Need to check multiple dependencies between resources...") 
        self.check_produced_needed_dependency(resources_needed)
        
    def getProduction_line(self, resource):
        return self.production_map[resource]
        
    def getCareful_needed_resources(self):
        return self.careful_needed_resources        
        
    def getProduced_resources(self):
        return self.production_map.keys()
    
    def getNeeded_resources(self, produced_resource):
        return self.production_map[produced_resource].production_need_list
        
    def enough_to_produce(self, stock):
        for item_to_produce in self.production_map.keys():
            production_line = self.production_map[item_to_produce]
            production_need_list = production_line.production_need_list
            produced_quantity = production_line.quantity_to_produce
            for prod_needed in production_need_list:
                needed_res_stock = prod_needed.quantity * produced_quantity
                #print("Trying to produce : "+item_to_produce.name +" with "+prod_needed.resource.name)
                avail_res_stock = stock.get_stock_for_resource(prod_needed.resource)
                if avail_res_stock < needed_res_stock:
                    return False
        return True
    
    def enough_stock_room(self, stock):
        for item_to_produce in self.production_map.keys():
            production_line = self.production_map[item_to_produce]
            quantity_to_produce = production_line.quantity_to_produce
            avail_room = stock.get_max_stock_for_resource(item_to_produce) - stock.get_stock_for_resource(item_to_produce)
            if avail_room < quantity_to_produce:
                return False
        return True
    
    def __str__(self):
        return "(Production rate)" + str(self.item_to_produce.name)  +  " to be produced at rate " + str(self.quantity)