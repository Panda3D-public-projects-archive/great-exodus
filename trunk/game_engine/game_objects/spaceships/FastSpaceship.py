'''
Created on 10 nov. 2011

@author: jerome
'''
from game_engine.game_objects.spaceships.Spaceship import Spaceship
from game_engine.game_objects.spaceships.SpaceshipsProperties import SpaceshipsProperties

class FastSpaceship(Spaceship):
    '''
    classdocs
    '''

    def __init__(self, name, coordinates, star_system_sector):
        '''
        Constructor
        '''
        super(FastSpaceship, self).__init__(name, coordinates, star_system_sector, SpaceshipsProperties.fast_speed)
        