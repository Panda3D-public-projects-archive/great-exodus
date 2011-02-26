# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''
from ResourcesPackage.Stock import Stock
from ResourcesPackage.StockLine import StockLine

class StockManager(object):
    '''
    classdocs
    '''


    def __init__(self, resource_manager):
        '''
        Constructor
        '''
        #Planets stocks
        self.small_wood_planet_stock = Stock([StockLine(resource_manager.wood, 10), ])
        self.medium_wood_planet_stock = Stock([StockLine(resource_manager.wood, 50),])
        self.large_wood_planet_stock = Stock([StockLine(resource_manager.wood, 250),])
        
        self.small_mineral_planet_stock = Stock([StockLine(resource_manager.stone, 10), ])
        self.medium_mineral_planet_stock = Stock([StockLine(resource_manager.stone, 100),])
        self.large_mineral_planet_stock = Stock([StockLine(resource_manager.stone, 250),])
        
        #Stations stocks
        #Paper stations
        self.small_paper_station_stock = Stock([StockLine(resource_manager.wood, 200), StockLine(resource_manager.paper, 20)])
        self.medium_paper_station_stock = Stock([StockLine(resource_manager.wood, 500),StockLine(resource_manager.paper, 100)])
        self.large_paper_station_stock = Stock([StockLine(resource_manager.wood, 2500),StockLine(resource_manager.paper, 500)])
               
        #Silex stations
        self.small_silex_station_stock = Stock([StockLine(resource_manager.stone, 100, 100), StockLine(resource_manager.silex, 10)])
        self.medium_silex_station_stock = Stock([StockLine(resource_manager.stone, 500, 350),StockLine(resource_manager.silex, 50)])
        self.large_silex_station_stock = Stock([StockLine(resource_manager.stone, 2500, 1500),StockLine(resource_manager.silex, 250)])