'''
Created on 10 nov. 2011

@author: jerome
'''
from game_engine.game_objects.GameObject import GameObject
from game_engine.PlayerStatus import PlayerStatus
from game_engine.GameStatus import GameStatus
from game_engine.displacement.MovementManager import MovementManager

class Galaxy(GameObject):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        super(Galaxy, self).__init__(name)
        self.star_systems_list = []
        
    def print_star_systems(self):
        print("Galaxy " + self.name + ":")
        for star_system in self.star_systems_list:
            print(star_system.name)
            
    def move_ships(self):
        if PlayerStatus.player_is_in_galaxy(self):
            for star_system in self.star_systems_list:
                star_system.move_ships()
        else:
            if GameStatus.actually_move:
                for star_system in self.star_systems_list:
                    star_system.move_ships_approximately()
                
    def add_star_system(self, star_system):
        self.star_systems_list.append(star_system)
    