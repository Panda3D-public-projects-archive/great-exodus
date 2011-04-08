# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''
from ResourcesPackage.ResourceNeed import ResourceNeed

class ProductionLine(ResourceNeed):
    '''
    classdocs
    '''


    def __init__(self, resource , quantity = 1 ):
        '''
        Constructor
        '''
        super(ProductionLine,self).__init__(resource,quantity)

    def __str__(self):
        return "["+self.resource.name+" : "+str(self.quantity)+"]"