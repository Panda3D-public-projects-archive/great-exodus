'''
Created on 2 dec. 2011

@author: jd219546
'''

class MoveObserver(object):
    '''
    classdocs
    '''


    def __init__(self, observer, observed):
        '''
        Constructor
        observer is GraphicsSpaceship
        observed is Spaceship
        '''
        self.observer = observer
        self.observed = observed
        observed.add_move_observer(self)
        
    def update_coordinates(self, coordinates):
        print "MoveObserver updating coordinates of  graphics observer of ",self.observed.get_name()
        self.observer.update_coordinates(coordinates)
        
    def remove_self_from_observed(self):
        self.observed.remove_move_observer(self)
    