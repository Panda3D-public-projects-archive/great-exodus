# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''
import math
from trunk.core.ResourcesPackage.StockLine import StockLine

class StockInfo(object):
    
    def __init__(self, quantity, max_stock):
        self.quantity = quantity
        self.max_stock = max_stock
        pass

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
            self.add_stock_line(i)
            #self.stock_dict[i.resource] = StockInfo(i.quantity, i.max_stock)
        
    def add_stock_line(self, stock_line):
        res = stock_line.resource
        if res not in self.stock_dict.keys():
            self.stock_dict[res] = StockInfo(stock_line.quantity,stock_line.max_stock)
        else:
            raise Exception("Key already in stock_dict in Stock")
        
    def print_stock(self, newline=False):
        for r in self.stock_dict.keys():
            print(r.name + " " + str(self.get_stock_for_resource(r)) + "/" + str(self.get_max_stock_for_resource(r)) + " ",end='')
        if newline: print("")
    
    def deepcopy(self):
        stock_lines = []
        for res in self.stock_dict.keys():
            quantity = self.get_stock_for_resource(res)
            max_stock = self.get_max_stock_for_resource(res)
            sl = StockLine( res, max_stock, quantity )
            stock_lines.append( sl )
        copy_stock = Stock(stock_lines)
        return copy_stock
   
    def get_stock_for_resource(self, res):
        return self.stock_dict[res].quantity
    
    def get_max_stock_for_resource(self,res,prop=1):
        return self.stock_dict[res].max_stock
    
    def increase_resource(self, prod_resource, prod_quantity ,prop=1):
        self.stock_dict[prod_resource].quantity += int(prod_quantity * prop)
        
    def decrease_resource(self, resource, quantity , prop=1):
        #self.check_used(prodObj)
        consuming = int(math.ceil(quantity * prop))
        self.stock_dict[resource].quantity -= consuming

    
    def has_resource(self, resource):
        return resource in self.stock_dict.keys()
    
    def __str__(self):
        return "(Stock)ressource : " + "\n(Stock)ressource : ".join(str(i.name) for i in self.stock_dict.keys())