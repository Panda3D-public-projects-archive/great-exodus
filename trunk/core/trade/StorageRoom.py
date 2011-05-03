'''
Created on 3 mai 2011

@author: benjamin
'''
from trunk.core.ResourcesPackage.StockManager import *
from trunk.core.ResourcesPackage.Stock import *

class StorageRoom(object):
    '''
    Should be moved to the package concerning ships and modules
    '''


    def __init__(self, stocks = None, is_docked = False):
        '''
        Constructor
        '''
        self.stocks = stocks
        
    def get_stocks(self):
        return self.stocks
    
    def get_is_docked(self):
        return self.is_docked
    
    def set_stocks(self, stocks):
        self.stocks = stocks
        
    def set_is_docked(self, is_docked):
        self.is_docked = is_docked
        
    def __str__(self):
        return "Storage room: " + self.stocks + " Docked: " + self.is_docked
        