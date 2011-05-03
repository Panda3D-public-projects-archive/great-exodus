# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''
from trunk.core.ResourcesPackage.Stock import Stock
from trunk.core.ResourcesPackage.StockLine import StockLine
import random

class StockManager(object):
    '''
    classdocs
    '''


    def __init__(self, resource_manager, default_stock_strategy = 0):
        '''
        Constructor
        '''
        self.default_stock_strategy = default_stock_strategy
        self.small_stock = 30
        #Planets stocks
        self.small_planet_stock = Stock([StockLine(resource_manager.ice, self.small_stock, self.default_stock()),StockLine(resource_manager.ore, self.small_stock, self.default_stock())])
        self.small_planet_stock_list = []

        self.small_factory_stock_list = []
        

    def default_stock(self):
        if self.default_stock_strategy == 0 :
            return 0
        else:
            return random.randint(0, self.small_stock)
        
    def create_small_factory_stock(self, production_rule):
        stock_lines = set()
        for item_to_produce in production_rule.getProduced_resources():
            stock_lines.add(StockLine(item_to_produce, self.small_stock, self.default_stock()))
            for production_need in production_rule.getNeeded_resources(item_to_produce):
                res_needed = production_need.resource
                stock_lines.add(StockLine(res_needed, self.small_stock, self.default_stock()))
        stock = Stock(stock_lines)
                
        self.add_small_factory_stock(stock)
        return stock
    
    def add_small_factory_stock(self, stock):
        self.small_factory_stock_list.append(stock)
        
    def create_small_planet_stock(self):
        stock = self.small_planet_stock.deepcopy()
        self.add_small_planet_stock(stock)
        return stock
    
    def add_small_planet_stock(self, stock):
        self.small_planet_stock_list.append(stock)
        
    def get_all_stocks(self):
        stock_list = []
        stock_list.extend(self.small_planet_stock_list)
        for l in self.small_factory_stock_list:
            stock_list.extend(l)
        return stock_list
        
    def print_global_stock(self):
        print("Small planets stocks: ")
        i = 1
        for s in self.small_planet_stock_list:
            s.print_stock()
            print (" | ",end='')
            i+=1
        print ("")
        print ("Small factories stocks: ")
        for r in self.small_factory_stock_list:
            print( "Small Factory Stock : ")
            r.print_stock()
            #print (" | ",end='')
            print ("")
            