'''
Created on 2 dec. 2011

@author: jd219546
'''
from gui.GraphicsObject import GraphicsObject
from gui.MoveObserver import MoveObserver

class GraphicsSpaceship(GraphicsObject):
    '''
    classdocs
    '''


    def __init__(self, ship):
        '''
        Constructor
        '''
        super(GraphicsSpaceship, self).__init__(ship.get_coordinates())
        self.move_observer = MoveObserver(self, ship)
        
    def remove_self_from_observed(self):
        self.move_observer.remove_self_from_observed()
        
        
        