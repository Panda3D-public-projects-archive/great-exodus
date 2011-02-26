# -*- coding: latin-1 -*-

'''
Created on 25 févr. 2011

@author: goungy
'''

import time

class ProductionObject(object):
    '''
    classdocs
    '''


    def __init__(self, stock, production_lines):
        '''
        Constructor
        '''
        self.stock = stock.deepcopy()
        #self.production_lines = production_lines
        for pr in production_lines:
            item_to_produce = pr.resource
            if not self.stock.has_resource(item_to_produce):
                raise Exception("Item to produce (" + str(item_to_produce.name) + ") does not exist in stock manager : " + str(self.stock))
            for needed_resource_line in item_to_produce.input_resource_lines:
                needed_resource = needed_resource_line.resource
                if not self.stock.has_resource(needed_resource):
                    raise Exception("Item to produce (" + str(item_to_produce.name) + ") needs ("+ str(needed_resource.name)+") which is not in stock manager : " + str(self.stock))
                
        self.production_lines_dict = {}
        for pl in production_lines:
            needed_resource_dict = {}
            for needed_resource_line in pl.resource.input_resource_lines:
                needed_resource = needed_resource_line.resource
                needed_quantity = needed_resource_line.quantity * pl.quantity
                needed_resource_dict[needed_resource] = needed_quantity
            self.production_lines_dict[pl.resource] = [ pl.quantity, needed_resource_dict]
            
        self.production_status = 0
            
    def print_stock(self):
        self.stock.print_stock()
        
    def can_produce(self):
        return self.production_status == 0
        
    def evolve_stock(self, production_resource):
        #print "EVOLVING "+production_resource.name+": " + str(self.stock.get_stock_for_resource(production_resource)) + " @ " + str(time.time()) + " s "
        prod_quantity = self.production_lines_dict[production_resource][0]
        needed_resource_dict = self.production_lines_dict[production_resource][1]
        enough_to_produce = True
        for needed_resource in needed_resource_dict.keys():
            needed_quantity = needed_resource_dict[needed_resource]
            avail_res = self.stock.get_stock_for_resource(needed_resource)
            if avail_res < needed_quantity:
                #print "Lacking " + str(needed_quantity - avail_res) + " " +needed_resource.name + " to produce " + production_resource.name
                enough_to_produce = False
                break
               
        if enough_to_produce:
            room_left = self.stock.get_max_stock_for_resource(production_resource) - self.stock.get_stock_for_resource(production_resource)
            if room_left:
                if room_left < prod_quantity:
                    prop_room_left = float(room_left) / prod_quantity
                else: prop_room_left = 1.
                for needed_resource in needed_resource_dict.keys():
                    self.stock.decrease_resource(needed_resource, needed_resource_dict[needed_resource],prop_room_left)
                self.stock.increase_resource(production_resource, prod_quantity, prop_room_left)
            else:
                self.production_status = 100 #print "Stock is full for " + production_resource.name
        else:
            self.production_status = 200# print "Cannot produce " + production_resource.name
        
    def __str__(self):
        return "(ProductionObject)\n" + str(self.stock) + "\n(Production)" + "\n(Production)".join(str(i) for i in self.production_lines)