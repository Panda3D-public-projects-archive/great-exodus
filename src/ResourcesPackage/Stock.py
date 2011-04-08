# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''
import math
from ResourcesPackage.StockLine import StockLine

class Stock(object):
    '''
    classdocs
    '''


    def __init__(self, stock_lines):
        '''
        Constructor
        '''
        #self.resource_lines = resource_lines
        self.stock_dict = {}
        
        for i in stock_lines:
            self.stock_dict[i.resource] = [ i.quantity, i.max_stock ]
            

        self.already_used = None

    def check_used(self, prodObj):
        if not self.already_used:
            self.already_used = prodObj
        else:
            if prodObj != self.already_used:
                raise Exception("STOCK ALREADY IN USE!!!")
        
    def print_stock(self, newline=False):
        for r in self.stock_dict.keys():
            print(r.name + " " + str(self.get_stock_for_resource(r)) + "/" + str(self.get_max_stock_for_resource(r)) + " ",end='')
        if newline: print("")
    
    def deepcopy(self):
        stock_lines = []
        for res in self.stock_dict.keys():
            quantity = self.stock_dict[res][0]
            max_stock = self.stock_dict[res][1]
            sl = StockLine( res, max_stock, quantity )
            stock_lines.append( sl )
        copy_stock = Stock(stock_lines)
        return copy_stock
   
    def get_stock_for_resource(self, res):
        return self.stock_dict[res][0]
    
    def get_max_stock_for_resource(self,res,prop=1):
        return self.stock_dict[res][1]
    
    def increase_resource(self, prod_resource, prod_quantity ,prop=1):
        self.stock_dict[prod_resource][0] += int(prod_quantity * prop)
        
    def decrease_resource(self, resource, quantity , prodObj, prop=1):
        #self.check_used(prodObj)
        consuming = int(math.ceil(quantity * prop))
        self.stock_dict[resource][0] -= consuming

    
    def has_resource(self, resource):
        return resource in self.stock_dict.keys()
    
    def __str__(self):
        return "(Stock)ressource : " + "\n(Stock)ressource : ".join(str(i.name) for i in self.stock_dict.keys())