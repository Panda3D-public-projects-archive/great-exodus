'''
Created on 10 nov. 2011

@author: jerome
'''
from game_engine.game_objects.GameObject import GameObject
from game_engine.PlayerStatus import PlayerStatus
from game_engine.displacement.MovementManager import MovementManager
from game_engine.GameStatus import GameStatus

class StarSystem(GameObject):
    '''
    classdocs
    '''


    def __init__(self, galaxy, name = None):
        '''
        Constructor
        '''
        super(StarSystem, self).__init__( name )
        self.star_system_sectors_list = []
        self.galaxy = galaxy
        
    def print_star_system_sectors(self):
        print("Star System " + self.name + ":")
        for star_system_sector in self.star_system_sectors_list:
            print(star_system_sector.name)
            
    def move_ships(self, actually_move = False):
        if PlayerStatus.player_is_in_star_system(self):
            i = 0
            for star_system_sector in self.star_system_sectors_list:
                if PlayerStatus.player_is_in_star_system_sector(star_system_sector):
                    star_system_sector.move_ships_random_accurately()
                else:
                    corresponding_subiter = i % GameStatus.subiterations
                    if corresponding_subiter == GameStatus.subiteration:
                        star_system_sector.move_ships_random_approximately()
                i += 1
        else:
            if GameStatus.actually_move:    
                self.move_ships_approximately()
    
    def move_ships_approximately(self):        
        i = 0
        for star_system_sector in self.star_system_sectors_list:
            corresponding_subiter = i % GameStatus.subiterations
            if corresponding_subiter == GameStatus.subiteration:
                #print(star_system_sector.name)
                star_system_sector.move_ships_random_approximately()
            i += 1
            
    def add_star_system_sector(self, star_system_sector):
        self.star_system_sectors_list.append(star_system_sector)