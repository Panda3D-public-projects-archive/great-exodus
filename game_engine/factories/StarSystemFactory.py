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
        self.star_systems_list = []
        
    def create_star_system(self, galaxy, name = None):
        if not name:
            name = "Star System " + str(len( self.star_systems_list))
        star_system = StarSystem(galaxy, name)            
        self.star_systems_list.append(star_system)
        galaxy.add_star_system(star_system)
        return star_system
        
StarSystemFactory = StarSystemFactory()
        