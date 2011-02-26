# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''

class ResourceNeed(object):
    '''
    classdocs
    '''


    def __init__(self, resource , quantity):
        '''
        Constructor
        '''
        self.resource = resource
        self.quantity = quantity

    def __str__(self):
        return "["+self.resource.name+" : "+str(self.quantity)+"]"