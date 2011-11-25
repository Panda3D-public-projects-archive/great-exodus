'''
Created on 18 nov. 2011

@author: JD219546
'''

class ShipProperties(object):
    '''
    classdocs
    '''


    def __init__(self, type, max_speed, max_hull, current_speed_ratio = 0, current_hull_ratio = 1):
        '''
        Constructor
        '''
        self.type = type
        self.max_speed = max_speed
        self.max_hull = max_hull
        self.current_speed_ratio = current_speed_ratio
        self.current_hull_ratio = current_hull_ratio
        