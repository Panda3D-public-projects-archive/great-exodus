# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''
from core.ResourcesPackage.ResourceNeed import ResourceNeed

class StockLine(ResourceNeed):
    '''
    classdocs
    '''


    def __init__(self, resource, max_stock, quantity=0):
        '''
        Constructor
        '''
        super(StockLine,self).__init__(resource, quantity)
        self.max_stock = max_stock