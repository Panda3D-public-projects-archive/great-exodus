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
        print "adding graphical item for ship",ship.get_name()," in player sector"
        g_spaceship = GraphicsSpaceship(ship)
        self.graphics_spaceship_list.append(g_spaceship)
        
    def destroy_all_ships(self):
        print "Player movement detected : destroying graphics items"
        for graph_ship in self.graphics_spaceship_list:
            graph_ship.remove_self_from_observed()
        del self.graphics_spaceship_list[:]
        #print "LIst after destruction :",len(self.graphics_spaceship_list)
        
GraphicsSpaceshipFactory = GraphicsSpaceshipFactory()