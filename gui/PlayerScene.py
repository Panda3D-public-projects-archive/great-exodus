'''
Created on 12 janv. 2012

@author: jerome
'''
from gui.GraphicsSpaceshipFactory import GraphicsSpaceshipFactory

class PlayerScene(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.graphics_ships = []
        
    def get_ships_from_sector(self, star_system_sector):
        GraphicsSpaceshipFactory.destroy_all_ships()
        for ship in star_system_sector.spaceships_list:
            GraphicsSpaceshipFactory.create_graphics_spaceship(ship)