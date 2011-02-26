# -*- coding: latin-1 -*-

'''
Created on 25 févr. 2011

@author: goungy
'''
from ProductionPackage.ProductionObject import ProductionObject
from ResourcesPackage.ProductionLine import ProductionLine
import threading

class ProductionTimer:
    def __init__(self, tempo, resource):
        self._target = self.evolve_stock
        self._tempo = tempo
        self.resource = resource
        self.production_object_list = []
        #self._timer = threading.Timer(self._tempo, self._run)

    def _run(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target()
        
    def start(self):
        if self.production_object_list:
            self._timer = threading.Timer(self._tempo, self._run)
            self._timer.start()

    def stop(self):
        self._timer.cancel()      
        
    def add_production_object(self, production_object):
        self.production_object_list.append(production_object)  
            
    def evolve_stock(self):
        production = 0
        for po in self.production_object_list:
            if po.can_produce():
                po.evolve_stock(self.resource)
                production += 1
        if production == 0:
            self.stop() 
            
    def is_running(self):
        return self._timer.isAlive()         

class ProductionManager(object):
    '''
    classdocs
    '''

    def create_small_silex_station(self, stock_manager):
        po = self.create_production_object( stock_manager.small_silex_station_stock, self.small_silex_station_production)
        self.small_silex_station_production_timer.add_production_object(po)

    def create_medium_silex_station(self, stock_manager):
        po = self.create_production_object( stock_manager.medium_silex_station_stock, self.medium_silex_station_production)
        self.medium_silex_station_production_timer.add_production_object(po)

    def create_large_silex_station(self, stock_manager):
        po = self.create_production_object( stock_manager.large_silex_station_stock, self.large_silex_station_production)
        self.large_silex_station_production_timer.add_production_object(po)

    def create_small_mineral_planet(self, stock_manager):
        po = self.create_production_object( stock_manager.small_mineral_planet_stock, self.small_mineral_planet_production)
        self.small_mineral_planet_production_timer.add_production_object(po)
    
    def create_medium_mineral_planet(self, stock_manager):
        po = self.create_production_object( stock_manager.medium_mineral_planet_stock, self.medium_mineral_planet_production)
        self.medium_mineral_planet_production_timer.add_production_object(po)
    
    def create_large_mineral_planet(self, stock_manager):
        po = self.create_production_object( stock_manager.large_mineral_planet_stock, self.large_mineral_planet_production)
        self.large_mineral_planet_production_timer.add_production_object(po)

    def create_small_wood_planet(self, stock_manager):
        po = self.create_production_object( stock_manager.small_wood_planet_stock, self.small_wood_planet_production)
        self.small_wood_planet_production_timer.add_production_object(po)
    
    def create_medium_wood_planet(self, stock_manager):
        po = self.create_production_object( stock_manager.medium_wood_planet_stock, self.medium_wood_planet_production)
        self.medium_wood_planet_production_timer.add_production_object(po)
    
    def create_large_wood_planet(self, stock_manager):
        po = self.create_production_object( stock_manager.large_wood_planet_stock, self.large_wood_planet_production)
        self.large_wood_planet_production_timer.add_production_object(po)

    def __init__(self, resource_manager):
        '''
        Constructor
        '''
        self.production_objects_list = []
        self.production_timers = []
        #defining timers
        self.small_silex_station_production_timer = ProductionTimer(2, resource_manager.silex)
        self.medium_silex_station_production_timer = ProductionTimer(4, resource_manager.silex)
        self.large_silex_station_production_timer = ProductionTimer(6, resource_manager.silex)
        
        self.small_mineral_planet_production_timer = ProductionTimer(1, resource_manager.stone)
        self.medium_mineral_planet_production_timer = ProductionTimer(2, resource_manager.stone)
        self.large_mineral_planet_production_timer = ProductionTimer(4, resource_manager.stone)
        
        self.small_wood_planet_production_timer = ProductionTimer(0.5, resource_manager.wood)
        self.medium_wood_planet_production_timer = ProductionTimer(1.75, resource_manager.wood)
        self.large_wood_planet_production_timer = ProductionTimer(2, resource_manager.wood)
        
        self.small_silex_station_production = [(ProductionLine(resource_manager.silex, 1)), ]
        self.medium_silex_station_production = [(ProductionLine(resource_manager.silex, 10)), ]
        self.large_silex_station_production = [(ProductionLine(resource_manager.silex, 65)), ]
              
        self.small_mineral_planet_production = [(ProductionLine(resource_manager.stone, 1)), ]
        self.medium_mineral_planet_production = [(ProductionLine(resource_manager.stone, 10)), ]
        self.large_mineral_planet_production = [(ProductionLine(resource_manager.stone, 50)), ]
        
        self.small_wood_planet_production = [(ProductionLine(resource_manager.wood, 2)), ]
        self.medium_wood_planet_production = [(ProductionLine(resource_manager.wood, 11)), ]
        self.large_wood_planet_production = [(ProductionLine(resource_manager.wood, 63)), ]
        
    def create_production_object(self, stock_manager, production_lines):
        po = ProductionObject(stock_manager, production_lines)
        return po
            
    def start_global_production(self):
        self.small_mineral_planet_production_timer.start()
        self.medium_mineral_planet_production_timer.start()
        self.large_mineral_planet_production_timer.start()
        self.small_wood_planet_production_timer.start()
        self.medium_wood_planet_production_timer.start()
        self.large_wood_planet_production_timer.start()
        self.small_silex_station_production_timer.start()
        self.medium_silex_station_production_timer.start()
        self.large_silex_station_production_timer.start()

    def is_global_production_stalled(self):
        still_running = (self.small_mineral_planet_production_timer.is_running() or
        self.medium_mineral_planet_production_timer.is_running() or 
        self.large_mineral_planet_production_timer.is_running() or 
        self.small_wood_planet_production_timer.is_running() or 
        self.medium_wood_planet_production_timer.is_running() or 
        self.large_wood_planet_production_timer.is_running() or 
        self.small_silex_station_production_timer.is_running() or 
        self.medium_silex_station_production_timer.is_running() or 
        self.large_silex_station_production_timer.is_running())

        return still_running == False
                   
    def __str__(self):
        return "Production Manager : \n" + "\n".join(str(i) for i in self.production_objects_list)