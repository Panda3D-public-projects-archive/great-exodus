'''
Created on 10 nov. 2011

@author: jerome
'''
from game_engine.game_objects.star_system_sectors.StarSystemSector import StarSystemSector

class StarSystemSectorFactory(object):
    '''
    classdocs
    '''
    def __call__(self):
        return self

    def __init__(self):
        '''
        Constructor
        '''
        self.star_systems_sectors_list = []
        
    def create_star_system_sector(self, star_system, name = None):   
        if not name:
            name = "Star System Sector " + str(len(self.star_systems_sectors_list))
        star_system_sector = StarSystemSector(star_system, name)
        self.star_systems_sectors_list.append(star_system_sector)
        star_system.add_star_system_sector(star_system_sector)
        
StarSystemSectorFactory = StarSystemSectorFactory()
        