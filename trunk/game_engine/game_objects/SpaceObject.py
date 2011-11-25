'''
Created on 10 nov. 2011

@author: jerome
'''
from game_engine.game_objects.GameObject import GameObject

class SpaceObject(GameObject):
    '''
    classdocs
    '''


    def __init__(self, name, coordinates, star_system_sector):
        '''
        Constructor
        '''
        super(SpaceObject, self).__init__(name)
        self.coordinates = coordinates
        self.star_system_sector = star_system_sector
        
    def __print__(self):
        return 'Name :'+ self.name+ 'Coordinates :'+ self.coordinates
    
    def __str__(self):
        return "Name : "+ self.name + " Coordinates : " + str(self.coordinates)

    def get_coordinates(self):
        return self.coordinates

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates
        
    def get_star_system_sector(self):
        return self.star_system_sector