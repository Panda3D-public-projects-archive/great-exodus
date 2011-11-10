'''
Created on 10 nov. 2011

@author: jerome
'''
from game_engine.game_objects.GameObject import GameObject

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
        