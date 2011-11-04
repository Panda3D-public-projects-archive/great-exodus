# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''

class Resource(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        
    def __str__(self):
        return self.name