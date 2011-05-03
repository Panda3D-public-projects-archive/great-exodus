'''
Created on 3 mai 2011

@author: benjamin
'''
from trunk.core.ResourcesPackage.StockManager import * 
from trunk.core.ResourcesPackage.Stock import *
from trunk.core.ResourcesPackage.StockLine import *

class StorageRoom(object):
    '''
    Should be moved to the package concerning ships and modules
    '''


    def __init__(self, stocks = None, is_docked = False):
        '''
        Constructor
        '''
        self.stocks = stocks
        self.is_docked = is_docked
        
    def get_stocks(self):
        return self.stocks
    
    def get_is_docked(self):
        return self.is_docked
    
    def set_stocks(self, stocks):
        self.stocks = stocks
        
    def set_is_docked(self, is_docked):
        self.is_docked = is_docked
        
    def __str__(self):
        if self.stocks != None:
            stocks_to_print = self.stocks
        else:
            stocks_to_print = "nothing"
        if self.is_docked :
            status_to_print = "yes"
        else:
            status_to_print = "no"
        return "Storage room: " + stocks_to_print + " ~~~ Docked: " + status_to_print
    
class StorageRoomTest(object):
    
    def main():
        storage_room = StorageRoom()
        print(str(storage_room))
        print("Let's display the stocks of the storage room :")
        print(str(storage_room.get_stocks()))
        print("Let's check that the storage room is not docked:")
        if storage_room.is_docked():
            to_print = "Ship docked."
        else:
            to_print = "Ship not docked."
        print(to_print)
        storage_room = None
        storage_room = StorageRoom(['Dildo', 69, 69], True)
        print(str(storage_room))
        if storage_room.is_docked():
            to_print = "Ship docked."
        else:
            to_print = "Ship not docked."
        print(to_print)
        print(str(storage_room.get_stocks()))
        storage_room.set_is_docked(False)
        storage_room.set_stocks(['Anal plug', 1, 1])
        print(str(storage_room))
        if storage_room.is_docked():
            to_print = "Ship docked."
        else:
            to_print = "Ship not docked."
        print(to_print)
        
    if __name__ == "__main__":
        main()
        pass
        