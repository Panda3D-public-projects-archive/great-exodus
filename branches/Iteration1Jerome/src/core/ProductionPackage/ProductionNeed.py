# -*- coding: latin-1 -*-
'''
Created on 25 fÃ©vr. 2011

@author: goungy
'''

class ProductionNeed(object):
    '''
    classdocs
    '''


    def __init__(self, resource , quantity = 1):
        '''
        Constructor
        '''
        self.resource = resource
        self.quantity = quantity

    def __str__(self):
        return "["+self.resource.name+" : "+str(self.quantity)+"]"