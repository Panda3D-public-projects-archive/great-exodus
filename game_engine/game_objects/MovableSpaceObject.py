'''
Created on 10 nov. 2011

@author: jerome
'''
from game_engine.displacement.Coordinates import Coordinates
from game_engine.game_objects.SpaceObject import SpaceObject

class MovableSpaceObject(SpaceObject):
    '''
    classdocs
    '''


    def __init__(self, name, coordinates, star_system_sector, speed):
        '''
        Constructor
        '''
        super(MovableSpaceObject, self).__init__(name, coordinates, star_system_sector)
        self.speed = speed
        
    def go_to_coord(self, coordinates):
        self.go_to_x_y_z(coordinates.get_x(), coordinates.get_y(), coordinates.get_z())
    
    def go_to_x_y_z(self, x, y, z):
        self.set_coordinates(Coordinates(x, y, z))   