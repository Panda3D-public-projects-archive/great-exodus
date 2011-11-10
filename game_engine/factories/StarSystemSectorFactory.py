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
        self.star_systems_sectors_dict = {}
        
    def create_star_system_sector(self, star_system, name = None):
        if not name:
            name = "Star System Sector " + str(len(self.star_systems_sectors_dict))
        star_system_sector = StarSystemSector(star_system, name)
        if not self.star_systems_sectors_dict.has_key(star_system):
            self.star_systems_sectors_dict[star_system] = []
        self.star_systems_sectors_dict[star_system].append(star_system_sector)
        
StarSystemSectorFactory = StarSystemSectorFactory()
        