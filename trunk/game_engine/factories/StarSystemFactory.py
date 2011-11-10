'''
Created on 10 nov. 2011

@author: jerome
'''
from game_engine.game_objects.star_systems.StarSystem import StarSystem

class StarSystemFactory(object):
    '''
    classdocs
    '''
    def __call__(self):
        return self

    def __init__(self):
        '''
        Constructor
        '''
        self.star_systems_dict = {}
        
    def create_star_system(self, galaxy, name = None):
        if not name:
            name = "Star System " + str(len(self.star_systems_dict))
        star_system = StarSystem(name)
        if not self.star_systems_dict.has_key(galaxy):
            self.star_systems_dict[galaxy] = []
        self.star_systems_dict[galaxy].append(star_system)
        
StarSystemFactory = StarSystemFactory()
        