'''
Created on 2 mai 2011

@author: benjamin
'''
from trunk.core.ResourcesPackage.Stock import *
from trunk.core.trade.Accounts import *
from trunk.core.trade.StockExchange import *

class Trader(object):
    '''
    This class models the action a trader can do.
    For the moment, a trader has a stock in order 
    to avoid conception problems (stocks will rather belong to ships).
    
    /!\ We should implement a method to check if the trader can sell, ie is docked
    to a planet or an entity that can buy/sell resources. /!\
    '''


    def __init__(self, accounts, stocks, resources_to_buy, resources_to_sell, can_trade = False):
        '''
        Constructor
        '''
        self.accounts = accounts
        self.stocks = stocks #should be the stocks of the ship
        self.resources_to_buy = resources_to_buy #to be defined by the player or the AI
        self.resources_to_sell = resources_to_sell #to be defined by the player or the AI
	self.can_trade = can_trade #a trader can only trade if he/she is docked to a station/factory/...
        
    def __str__(self):
        return self.accounts + " " + self.stocks + " " + self.resources_to_buy + " " + self.resources_to_sell
    
    def get_accounts(self):
        return self.accounts
    
    def get_stocks(self):
        return self.stocks
    
    def get_resources_to_buy(self):
        return self.resources_to_buy
    
    def get_resources_to_sell(self):
        return self.resources_to_sell

    def get_can_trade(self):
	return self.can_trade
    
    def set_accounts(self, accounts):
        self.accounts = accounts
        
    def set_stocks(self, stocks):
        self.stocks = stocks
        
    def set_resources_to_buy(self, resources_to_buy):
        self.resources_to_buy = resources_to_buy
        
    def set_resources_to_sell(self, resources_to_sell):
        self.resources_to_sell = resources_to_sell

    def set_can_trade(self, can_trade):
	self.can_trade = can_trade
        
    def buy(self, resource, quantity):
        if self.get_can_trade() and resource.price()*quantity <= self.accounts.get_credits() and quantity + self.stocks.get_stock_for_resource(resource) <= self.stocks.get_max_stock_for_resource(resource):
            self.accounts.decrease(resource.price()*quantity)
            self.stocks.increase_resource(resource, quantity)
        else:
            raise Exception("Can not buy this resource.")
        
    def sell(self, resource, quantity):
        if self.get_can_trade() and quantity < self.stocks.get_stock_for_resource(resource):
            self.accounts.increase(resource.price()*quantity)
            self.stocks.decrease_resource(resource, quantity)
        else:
            raise Exception("Can not sell this resource.")
        
    
        
