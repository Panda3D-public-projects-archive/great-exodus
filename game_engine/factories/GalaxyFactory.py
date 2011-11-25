'''
Created on 10 nov. 2011

@author: jerome
'''
from game_engine.game_objects.galaxies.Galaxy import Galaxy

class GalaxyFactory(object):
    '''
    classdocs
    '''
    def __call__(self):
        return self

    def __init__(self):
        '''
        Constructor
        '''
        self.galaxies_list = []
        
    def create_galaxy(self, name = None):
        if not name :
            name = "Galaxy " + str(len(self.galaxies_list))
        galaxy = Galaxy(name)
        self.galaxies_list.append(galaxy)
        return galaxy
        
GalaxyFactory = GalaxyFactory()