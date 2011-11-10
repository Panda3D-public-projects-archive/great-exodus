'''
Created on 10 nov. 2011

@author: jerome
'''
from game_engine.game_objects.GameObject import GameObject

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