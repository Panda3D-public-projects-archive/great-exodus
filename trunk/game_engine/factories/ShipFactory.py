'''
Created on 9 nov. 2011

@author: JD219546
'''

from game_engine.displacement.Coordinates import Coordinates
from game_engine.game_objects.database.ShipsDatabase import ShipsDatabase
from game_engine.game_objects.spaceships.Spaceship import Spaceship
from gui.GraphicsSpaceshipFactory import GraphicsSpaceshipFactory


class ShipFactory(object):
    '''
    classdocs
    '''
    
    CARGO = "Cargo"
    SCOUT = "Scout"
    
    def __call__(self):
        return self
    
    def __init__(self):
        '''
        Constructor
        '''
        self.ship_list = []           
        
    def create_ship(self, name, coordinates, star_system_sector, ship_properties):
        ship = Spaceship(name, coordinates, star_system_sector, ship_properties)
        GraphicsSpaceshipFactory.create_graphics_spaceship(ship)
        self.ship_list.append(ship)
        star_system_sector.add_spaceship(ship)
        
    '''  
    def create_cargo_in_star_system(self, star_system_sector, name = None, coordinates = Coordinates(0, 0, 0)):
        if not name:
            name = "Cargo "+str(self.number_of_ships())
        ship_properties = ShipsDatabase.get_ship_info_from_type(self.CARGO)
        return self.create_ship(name, coordinates, star_system_sector, ship_properties)
        
    def create_scout_in_star_system(self, star_system_sector, name = None, coordinates = Coordinates(0, 0, 0)):
        if not name:
            name = "Scout "+str(self.number_of_ships())
        ship_properties = ShipsDatabase.get_ship_info_from_type(self.SCOUT)
        return self.create_ship(name, coordinates, star_system_sector, ship_properties)
    '''    
    def get_ship_list(self):
        return self.ship_list
        
    def number_of_ships(self):
        return len(self.ship_list)
    
ShipFactory = ShipFactory()