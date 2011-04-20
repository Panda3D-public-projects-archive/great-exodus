# -*- coding: latin-1 -*-

'''
Created on 25 févr. 2011

@author: goungy
'''

from core.ProductionPackage.ProductionLine import ProductionLine

class ProductionObject(object):
    '''
    classdocs
    '''


    def __init__(self, stock, production_resource_list, production_timer_factory):
        '''
        Constructor
        '''
        self.stock = stock
        self.production_status = {}
        #self.production_lines = production_lines
        for pr in production_resource_list:
            item_to_produce = pr
            if not self.stock.has_resource(item_to_produce):
                raise Exception("Item to produce (" + str(item_to_produce.name) + ") does not exist in stock manager : " + str(self.stock))
            for needed_resource_line in item_to_produce.input_resource_lines:
                needed_resource = needed_resource_line.resource
                if not self.stock.has_resource(needed_resource):
                    raise Exception("Item to produce (" + str(item_to_produce.name) + ") needs ("+ str(needed_resource.name)+") which is not in stock manager : " + str(self.stock))
            self.production_status[item_to_produce] = 0    
                
        self.production_lines_dict = {}
        for pl in production_resource_list:
            needed_resource_dict = {}
            for needed_resource_line in pl.input_resource_lines:
                needed_resource = needed_resource_line.resource
                needed_quantity = needed_resource_line.quantity * pl.output_production
                needed_resource_dict[needed_resource] = needed_quantity
            self.production_lines_dict[pl] = ProductionLine(needed_resource_dict, production_timer_factory.time_interval_dict[pl],pl.output_production)
            #self.production_lines_dict[pl].iterations_to_wait = 0
            
        
    """            
    def print_stock(self):
        self.stock.print_stock()
    """
    def update(self, iteration):
        for res_prod in self.production_lines_dict.keys():
            if iteration % self.production_lines_dict[res_prod].production_time_interval == 0:
                self.evolve_stock(res_prod)
       
    def getProduced_resources(self):
        return self.production_lines_dict.keys()
        
    def can_produce(self, resource):
        return self.production_status[resource] == 0
        
    def evolve_stock(self, production_resource):
        #print "EVOLVING "+production_resource.name+": " + str(self.stock.get_stock_for_resource(production_resource)) + " @ " + str(time.time()) + " s "
        #self.stock.print_stock()
        prod_quantity = self.production_lines_dict[production_resource].quantity_to_produce
        needed_resource_dict = self.production_lines_dict[production_resource].needed_resources_dict
        enough_to_produce = True
        for needed_resource in needed_resource_dict.keys():
            needed_quantity = needed_resource_dict[needed_resource]# * prod_quantity
            avail_res = self.stock.get_stock_for_resource(needed_resource)
            if avail_res < needed_quantity:
                #print "Lacking " + str(needed_quantity - avail_res) + " " +needed_resource.name + " to produce " + production_resource.name
                enough_to_produce = False
                break
               
        if enough_to_produce:
            room_left = self.stock.get_max_stock_for_resource(production_resource) - self.stock.get_stock_for_resource(production_resource)
            if room_left:
                if room_left < prod_quantity:
                    self.production_status[production_resource] = 300
                    #prop_room_left = float(room_left) / prod_quantity
                else: 
                    prop_room_left = 1.
                    for needed_resource in needed_resource_dict.keys():
                        self.stock.decrease_resource(needed_resource, needed_resource_dict[needed_resource],self,prop_room_left)
                    self.stock.increase_resource(production_resource, prod_quantity, prop_room_left)
            else:
                self.production_status[production_resource] = 100 #print "Stock is full for " + production_resource.name
        else:
            self.production_status[production_resource] = 200# print "Cannot produce " + production_resource.name
        #print "EVOLVED"
        #self.stock.print_stock()
        
    def __str__(self):
        return "(ProductionObject)\n" + str(self.stock) + "\n(Production)" + "\n(Production)".join(str(i) for i in self.production_lines)