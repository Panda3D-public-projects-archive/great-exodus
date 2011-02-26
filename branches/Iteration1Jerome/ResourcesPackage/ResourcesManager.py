# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''
from ResourcesPackage.Resource import Resource
from ResourcesPackage.ResourceNeed import ResourceNeed

class ResourcesManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.wood = Resource("wood")
        self.junk = Resource("junk")
        self.stone = Resource("stone")
        self.paper = Resource("paper",[ResourceNeed(self.wood,10),])
        self.silex = Resource("silex",[ResourceNeed(self.stone,5),])