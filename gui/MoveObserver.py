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
        '''
        self.observer = observer
        self.observed = observed
        observed.add_move_observer(self)
        
    def update_coordinates(self, coordinates):
        print "MoveObserver updating",self.observed.get_name()
        self.observer.update_coordinates(coordinates)
    