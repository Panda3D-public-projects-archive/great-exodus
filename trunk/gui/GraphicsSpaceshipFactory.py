'''
Created on 2 dec. 2011

@author: jd219546
'''
from gui.GraphicsSpaceship import GraphicsSpaceship

class GraphicsSpaceshipFactory():
    '''
    classdocs
    '''

    def __call__(self):
        return self

    def __init__(self):
        '''
        Constructor
        '''
        self.graphics_spaceship_list = []
        
    def create_graphics_spaceship(self, ship):
        g_spaceship = GraphicsSpaceship(ship)
        self.graphics_spaceship_list.append(g_spaceship)
        
GraphicsSpaceshipFactory = GraphicsSpaceshipFactory()