'''
Created on 2 mai 2011

@author: benjamin
'''
from core.ResourcesPackage.Stock import *
from core.ResourcesPackage.StockLine import *
from core.trade.Accounts import *
from core.trade.StockExchange import *
from core.trade.StorageRoom import * #will be in "space"
from core.trade.Entity import *
from core.trade.StockExchange import *

class Trader(object):
    '''
    This class models the action a trader can do.
    For the moment, a trader has a stock in order 
    to avoid conception problems (stocks will rather belong to ships).
    
    /!\ We should implement a method to check if the trader can sell, ie is docked
    to a planet or an entity that can buy/sell resources. /!\
    '''

    def __init__(self, accounts, storage_room, resources_to_buy = None, resources_to_sell = None, entity_to_trade_with = None, stock_exchange = None):
        '''
        Constructor
        '''
        self.accounts = accounts
        self.storage_room = storage_room
        self.resources_to_buy = []
        self.resources_to_buy.append(resources_to_buy) #to be defined by the player or the AI // is a list [Resource, quantity]
        self.resources_to_sell = [] 
        self.resources_to_sell.append(resources_to_sell) #to be defined by the player or the AI // is a list
        self.is_docked = self.storage_room.get_is_docked() #temporary boolean to test wether the trader is at a station or not / to be removed
        self.entity_to_trade_with = entity_to_trade_with
        self.stock_exchange = stock_exchange
        
    def __str__(self):
        return str(self.accounts) + " " + str(self.storage_room) + " " + str(self.resources_to_buy) + " " + str(self.resources_to_sell) + " " + str(self.is_docked) + str(self.entity_to_trade_with) + str(self.stock_exchange)
    
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
    
    def get_entity_to_trade_with(self):
        return self.entity_to_trade_with
    
    def get_stock_exchange(self):
        return self.stock_exchange
    
    def set_accounts(self, accounts):
        self.accounts = accounts
        
    def set_storage_room(self, storage_room):
        self.storage_room = storage_room
        self.is_docked = storage_room.get_is_docked()
        
    def set_resources_to_buy(self, resources_to_buy):
        self.resources_to_buy = resources_to_buy
        
    def set_resources_to_sell(self, resources_to_sell):
        self.resources_to_sell = resources_to_sell
        
    def set_is_docked(self, is_docked):
        self.is_docked = is_docked
        
    def set_entity_to_trade_with(self, entity_to_trade_with):
        self.entity_to_trade_with = entity_to_trade_with
        
    def set_stock_exchange(self, stock_exchange):
        self.stock_exchange = stock_exchange
        
    def add_resource_to_buy(self, resource, quantity):
        self.resources_to_buy.append([resource, quantity])
        
    def add_resource_to_sell(self, resource, quantity):
        self.resources_to_sell.append([resource, quantity])
        
    def buy(self, resource, quantity):
        if self.is_docked and self.stock_exchange.get_price(resource)*quantity <= self.accounts.get_credits() and quantity + self.storage_room.get_stocks().get_stock_for_resource(resource) <= self.storage_room.get_stocks().get_max_stock_for_resource(resource) and quantity <= self.entity_to_trade_with.get_stocks().get_stock_for_resource(resource):
            self.accounts.decrease(self.stock_exchange.get_price(resource)*quantity)
            self.entity_to_trade_with.get_accounts().increase(self.stock_exchange.get_price(resource)*quantity)
            self.storage_room.get_stocks().increase_resource(resource, quantity)
            self.entity_to_trade_with.get_stocks().decrease_resource(resource, quantity)
        else:
            raise Exception("Can not buy this resource.")
        
    def sell(self, resource, quantity):
        if self.is_docked and quantity < self.storage_room.get_stocks().get_stock_for_resource(resource) and self.stock_exchange.get_price(resource)*quantity <= self.entity.get_accounts().get_credits() and quantity + self.entity_to_trade_with.get_stocks().get_stock_for_resource(resource) <= self.entity_to_trade_with.get_stocks().get_max_stock_for_resource(resource) :
            self.accounts.increase(self.stock_exchange.get_price(resource)*quantity)
            self.entity_to_trade_with.get_accounts().decrease(self.stock_exchange.get_price(resource)*quantity)
            self.storage_room.get_stocks().decrease_resource(resource, quantity)
            self.entiry_to_trade_with.get_stocks().increade_resource(resource, quantity)
        else:
            raise Exception("Can not sell this resource.")
        
        
class TestTrader(object):
    
    def main():
        trader = Trader(Accounts(9000), StorageRoom(Stock({StockLine(Resource("Dildo"), 69, 10)})))
        print(str(trader))
        entity = Entity("La grosse bite à Dudule", Stock({StockLine(Resource("Dildo"), 69, 10)}), Accounts(2000))
        print(str(entity))
        stock_exchange = StockExchange()
        trader.set_stock_exchange(stock_exchange)
        trader.set_entity_to_trade_with(entity)
        print(str(trader.get_entity_to_trade_with()))
        trader.set_is_docked(True)
        print(str(trader.get_is_docked()))
        trader.add_resource_to_buy(Resource("Dildo"), 10)
        trader.add_resource_to_sell(Resource("Dildo"), 10)
        print(str(trader.get_resources_to_buy()))
        print(str(trader.get_resources_to_sell()))
        trader.buy(Resource("Dildo"), 10)
        print(str(trader))
        print(str(entity))
        trader.sell(Resource("Dildo"),10)
        print(str(trader))
        print(str(entity))
    
    if __name__ == "__main__":
        main()
        pass
        
    
        