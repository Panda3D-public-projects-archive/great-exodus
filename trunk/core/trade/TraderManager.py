'''
Created on 2 mai 2011

@author: benjamin
'''

from trunk.core.trade import Trader

class TraderManager(object):
    '''
    Manager
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.trader_list = []
        
    def __str__(self):
        for trader in self.trader_list:
            return self.trader_list[trader]
        
    def get_trader_list(self):
        return self.trader_list
    
    def set_trader_list(self, trader_list):
        self.trader_list = trader_list
        
    def add_trader(self, trader):
        self.trader_list.append(trader)
        
    def create_trader(self, accounts, storage_room, resources_to_buy = False, resources_to_sell = False, is_docked):
        trader = Trader(accounts, storage_room, resources_to_buy, resources_to_sell, is_docked)
        self.add_trader(trader)
        return trader