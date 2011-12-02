'''
Created on 2 dec. 2011

@author: jd219546
'''

class GraphicsObject(object):
    '''
    classdocs
    '''


    def __init__(self, coordinates):
        '''
        Constructor
        '''
        self.coordinates = coordinates
    
    def update_coordinates(self, coordinates):
        print "Updating coordinates"
        