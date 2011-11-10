'''
Created on 9 nov. 2011

@author: JD219546
'''

from game_engine.displacement.Coordinates import Coordinates
from game_engine.game_objects.spaceships.SlowSpaceship import SlowSpaceship
from game_engine.game_objects.spaceships.FastSpaceship import FastSpaceship

class ShipFactory(object):
    '''
    classdocs
    '''
    def __call__(self):
        return self
    
    def __init__(self):
        '''
        Constructor
        '''
        self.ship_list = []
        
    def create_slow_ship_in_star_system(self, star_system_sector, name = None, coordinates = Coordinates(0, 0, 0)):
        if not name:
            name = "Slow Spaceship "+str(self.number_of_ships())            
        ship = SlowSpaceship(name, coordinates, star_system_sector)
        #print(ship)
        self.ship_list.append(ship)
        star_system_sector.add_spaceship(ship)
        
    def create_fast_ship_in_star_system(self, star_system_sector, name = None, coordinates = Coordinates(0, 0, 0)):
        if not name:
            name = "Fast Spaceship "+str(self.number_of_ships())            
        ship = FastSpaceship(name, coordinates, star_system_sector)
        #print(ship)
        self.ship_list.append(ship)
        star_system_sector.add_spaceship(ship)
        
    def get_ship_list(self):
        return self.ship_list
        
    def number_of_ships(self):
        return len(self.ship_list)
    
ShipFactory = ShipFactory()