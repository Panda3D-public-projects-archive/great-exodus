'''
Created on 10 nov. 2011

@author: jerome
'''
from game_engine.game_objects.GameObject import GameObject
from game_engine.PlayerStatus import PlayerStatus
from game_engine.displacement.MovementManager import MovementManager
from game_engine.GameStatus import GameStatus

class StarSystemSector(GameObject):
    '''
    classdocs
    '''

    def __init__(self, star_system, name):
        '''
        Constructor
        '''
        self.star_system = star_system
        super(StarSystemSector, self).__init__(name)
        self.spaceships_list = []
        
    def add_spaceship(self, spaceship):
        self.spaceships_list.append(spaceship)
        
    def print_spaceships(self):
        print("Star System Sector " + self.name)
        for spaceship in self.spaceships_list:
            print(spaceship.name)
    """
    def move_ships(self, actually_move = False):
        if PlayerStatus.player_is_in_star_system_sector(self):
                MovementManager.move_ships_random_accurately(self.spaceships_list)
        else:
            self.move_ships_approximately()
    """
    def move_ships_random_approximately(self):
            MovementManager.move_ships_random_approximately(self.spaceships_list)
            
    def move_ships_random_accurately(self):
            MovementManager.move_ships_random_accurately(self.spaceships_list)            
