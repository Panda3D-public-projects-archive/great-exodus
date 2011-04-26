# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''

class StockLine(object):
    '''
    classdocs
    '''


    def __init__(self, resource, max_stock, quantity=0):
        '''
        Constructor
        '''
        self.resource = resource
        self.quantity = quantity
        self.max_stock = max_stock