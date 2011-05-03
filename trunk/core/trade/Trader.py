'''
Created on 2 mai 2011

@author: benjamin
'''
from trunk.core.ResourcesPackage.Stock import *
from trunk.core.trade.Accounts import *
from trunk.core.trade.StockExchange import *
from trunk.core.trade.StorageRoom import * #will be in "space"

class Trader(object):
    '''
    This class models the action a trader can do.
    For the moment, a trader has a stock in order 
    to avoid conception problems (stocks will rather belong to ships).
    
    /!\ We should implement a method to check if the trader can sell, ie is docked
    to a planet or an entity that can buy/sell resources. /!\
    '''

    def __init__(self, accounts, storage_room, resources_to_buy = None, resources_to_sell = None, is_docked = False):
        '''
        Constructor
        '''
        self.accounts = accounts
        self.storage_room = storage_room
        self.resources_to_buy = resources_to_buy #to be defined by the player or the AI
        self.resources_to_sell = resources_to_sell #to be defined by the player or the AI
        self.is_docked = self.storage_room().is_docked() #temporary boolean to test wether the trader is at a station or not / to be removed
        
    def __str__(self):
        return self.accounts + " " + self.storage_room + " " + self.resources_to_buy + " " + self.resources_to_sell + " " + self.is_docked
    
    def get_accounts(self):
        return self.accounts
    
    def get_storage_room(self):
        return self.storage_room
    
    def get_resources_to_buy(self):
        return self.resources_to_buy
    
    def get_resources_to_sell(self):
        return self.resources_to_sell
    
    def get_is_docked(self):
        return self.is_docked
    
    def set_accounts(self, accounts):
        self.accounts = accounts
        
    def set_storage_room(self, storage_room):
        self.storage_room = storage_room
        
    def set_resources_to_buy(self, resources_to_buy):
        self.resources_to_buy = resources_to_buy
        
    def set_resources_to_sell(self, resources_to_sell):
        self.resources_to_sell = resources_to_sell
        
    def set_is_docked(self, is_docked):
        self.is_docked = is_docked
        
    def buy(self, resource, quantity):
        if self.is_docked and resource.price()*quantity <= self.accounts.get_credits() and quantity + self.stocks.get_stock_for_resource(resource) <= self.stocks.get_max_stock_for_resource(resource):
            self.accounts.decrease(resource.price()*quantity)
            self.storage_room.get_stocks().increase_resource(resource, quantity)
        else:
            raise Exception("Can not buy this resource.")
        
    def sell(self, resource, quantity):
        if self.is_docked and quantity < self.stocks.get_stock_for_resource(resource):
            self.accounts.increase(resource.price()*quantity)
            self.storage_room.get_stocks().decrease_resource(resource, quantity)
        else:
            raise Exception("Can not sell this resource.")
        
    
        