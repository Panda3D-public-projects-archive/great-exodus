# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''

class ProductionRate(object):
    '''
    classdocs
    '''


    def __init__(self, item_to_produce, quantity):
        '''
        Constructor
        '''
        self.item_to_produce = item_to_produce
        self.quantity = quantity
        
    def __str__(self):
        return "(Production rate)" + str(self.item_to_produce.name)  +  " to be produced at rate " + str(self.quantity)