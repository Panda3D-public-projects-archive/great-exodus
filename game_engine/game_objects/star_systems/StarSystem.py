'''
Created on 10 nov. 2011

@author: jerome
'''
from game_engine.game_objects.GameObject import GameObject

class StarSystem(GameObject):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        super(StarSystem, self).__init__(name)
        self.star_system_sectors_list = []
        
    def print_star_system_sectors(self):
        print("Star System " + self.name + ":")
        for star_system_sector in self.star_system_sectors_list:
            print(star_system_sector.name)        