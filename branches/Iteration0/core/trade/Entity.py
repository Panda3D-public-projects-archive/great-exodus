'''
Created on 4 mai 2011

@author: benjamin
'''
from core.ResourcesPackage.Stock import *
from core.ResourcesPackage.StockLine import *
from core.ResourcesPackage.Resource import *
from core.trade.Accounts import *

class Entity(object):
    '''
    To represent all the "entities" able to trade
    '''


    def __init__(self, name, stocks, accounts):
        '''
        Constructor
        '''
        self.name = name
        self.stocks = stocks
        self.accounts = accounts
        
    def __str__(self):
        return "Entity: " + str(self.name) + " Stocks: " + str(self.stocks) + " " + str(self.accounts)
        
    def get_name(self):
        return self.name
    
    def get_stocks(self):
        return self.stocks
    
    def get_accounts(self):
        return self.accounts
    
    def set_name(self, name):
        self.name = name
        
    def set_stocks(self, stocks):
        self.stocks = stocks
        
    def set_accounts(self, accounts): 
        self.accounts = accounts

class TestEntity(object):
    
    def main():
        entity = Entity("La grosse bite à Dudule", Stock({StockLine(Resource("Dildo"), 69, 69)}), Accounts(69))
        print(str(entity))
        entity.set_name("Roger")
        print("Entity name: " + entity.get_name())
        entity.set_stocks(Stock({StockLine(Resource("Cockring"), 10, 9)}))
        print("Entity stocks: " + str(entity.get_stocks()))
        entity.set_accounts(Accounts(879997979879))
        print("Entity accounts: " + str(entity.get_accounts()))
    
    if __name__ == "__main__":
        main()
        pass