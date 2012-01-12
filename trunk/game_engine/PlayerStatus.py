'''
Created on 13 nov. 2011

@author: JD219546
'''
from game_engine.displacement.MovementManager import MovementManager

class PlayerStatus(object):
    '''
    classdocs
    '''
    def __call__(self):
        return self

    def __init__(self):
        '''
        Constructor
        '''
        self.current_galaxy = None
        self.current_star_system = None
        self.current_star_system_sector = None
        
        self.player_move_observer = None
        
    def set_position_in_universe(self, current_star_system_sector):          
        self.current_star_system_sector = current_star_system_sector
        self.current_star_system = self.current_star_system_sector.star_system
        self.current_galaxy = self.current_star_system.galaxy
        MovementManager.update_movement_lists(current_star_system_sector)
        self.player_move_observer.update_position_in_universe(self.current_star_system_sector)
        

    def player_is_in_galaxy(self, galaxy):
        return galaxy == self.current_galaxy
    
    def player_is_in_star_system(self, star_system):
        return star_system == self.current_star_system
    
    def player_is_in_star_system_sector(self, star_system_sector):
        return star_system_sector == self.current_star_system_sector

    def set_player_move_observer(self, observer):
        self.player_move_observer = observer

PlayerStatus = PlayerStatus()