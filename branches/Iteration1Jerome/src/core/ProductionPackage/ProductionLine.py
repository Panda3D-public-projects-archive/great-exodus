# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''

class ProductionLine(object):
    '''
    classdocs
    '''


    def __init__(self, needed_resources_dict , production_time_interval, quantity_to_produce = 1 ):
        '''
        Constructor
        '''
        self.quantity_to_produce = quantity_to_produce
        self.needed_resources_dict = needed_resources_dict
        self.production_time_interval = production_time_interval

    def __str__(self):
        return "["+self.resource.name+" : "+str(self.quantity)+"]"