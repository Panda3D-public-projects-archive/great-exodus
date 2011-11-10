'''
Created on 4 nov. 2011

@author: JD219546
'''
from game_engine.factories.ShipFactory import ShipFactory
from game_engine.displacement.MovementManager import MovementManager
from game_engine.factories.GalaxyFactory import GalaxyFactory
from game_engine.game_objects.star_systems.StarSystem import StarSystem
from game_engine.factories.StarSystemFactory import StarSystemFactory
from game_engine.factories.StarSystemSectorFactory import StarSystemSectorFactory

class GameEngine(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.movement_manager = MovementManager()
        
    def update(self, iteration_number):
        ship_list = ShipFactory.get_ship_list()
        i = 0
        for ship in ship_list:
            self.movement_manager.move_ship_random(ship)
            if i < 10 : print(ship)
            i += 1
        pass
    '''
    Help function to create ships for testing.
    Will not be part of final project.
    '''
    def create_ships_in_star_system_sector(self, star_system_sector, nb_ships = 0):
        for i in range(nb_ships):
            ShipFactory.create_slow_ship_in_star_system(star_system_sector)
            ShipFactory.create_fast_ship_in_star_system(star_system_sector)
            
    def create_galaxies(self, nb_galaxies = 1):
        for i in range(nb_galaxies):
            GalaxyFactory.create_galaxy()
            
    def create_star_systems(self, galaxy, nb_star_systems = 1):
        for i in range(nb_star_systems):
            StarSystemFactory.create_star_system(galaxy)
            
    def create_star_system_sectors(self, star_system, nb_star_system_sectors = 1):
        for i in range(nb_star_system_sectors):
            StarSystemSectorFactory.create_star_system_sector(star_system)