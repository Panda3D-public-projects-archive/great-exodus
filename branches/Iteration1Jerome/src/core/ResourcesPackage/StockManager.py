# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''
from core.ResourcesPackage.Stock import Stock
from core.ResourcesPackage.StockLine import StockLine
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
        
        #to build automatically factories stocks
        self.small_factory_default_stock = {}
        for res in resource_manager.resource_list:
            stockLine_list = [StockLine(res, self.small_stock),]
            for need_res in res.get_needed_resources():
                stockLine_list.append(StockLine(need_res, self.small_stock, self.default_stock()))
            self.small_factory_default_stock[res] = Stock(stockLine_list)
            
        self.small_factory_stock_map = {}
        

    def default_stock(self):
        if self.default_stock_strategy == 0 :
            return 0
        else:
            return random.randint(0, self.small_stock)
        
    def create_small_factory_stock(self, resource):
        stock = self.small_factory_default_stock[resource].deepcopy()
        stock.stock_dict[resource][0] = self.default_stock()
        self.add_small_factory_stock(resource,stock)
        return stock
    
    def add_small_factory_stock(self, resource, stock):
        if resource not in self.small_factory_stock_map.keys():
            self.small_factory_stock_map[resource] = []
        self.small_factory_stock_map[resource].append(stock)
        
    def create_small_planet_stock(self):
        stock = self.small_planet_stock.deepcopy()
        self.add_small_planet_stock(stock)
        return stock
    
    def add_small_planet_stock(self, stock):
        self.small_planet_stock_list.append(stock)
        
    def get_all_stocks(self):
        stock_list = []
        stock_list.extend(self.small_planet_stock_list)
        for l in self.small_factory_stock_map.values():
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
        for r in self.small_factory_stock_map.keys():
            print( "Small",r.name,"Factories Stocks : ")
            for f in self.small_factory_stock_map[r]:
                f.print_stock()
                print (" | ",end='')
            print ("")
            