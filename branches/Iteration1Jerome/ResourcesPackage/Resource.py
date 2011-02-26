# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''

class Resource(object):
    '''
    classdocs
    '''


    def __init__(self, name, input_resource_lines = []):
        '''
        Constructor
        '''
        self.input_resource_lines = input_resource_lines
        self.name = name
        
    def __str__(self):
        if self.input_resources:
            return self.name + " needs resource(s) : " + ", ".join(str(i.resource.name) + "=>" + str(i.quantity) for i in self.input_resource_lines)
        else:
            return self.name + " needs no resource"