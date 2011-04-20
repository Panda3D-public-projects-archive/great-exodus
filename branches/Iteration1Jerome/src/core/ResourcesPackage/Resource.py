# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''

class Resource(object):
    '''
    classdocs
    '''


    def __init__(self, name, output_production = 1, input_resource_lines = []):
        '''
        Constructor
        '''
        #input_resource_lines is a list of ResourceNeed
        self.input_resource_lines = input_resource_lines
        self.output_production = output_production
        self.name = name
        self.output_production = output_production
        
    def get_needed_resources(self):
        needed_resoucres_list = []
        for res_need in self.input_resource_lines:
            needed_resoucres_list.append(res_need.resource)
        return needed_resoucres_list
        
    def __str__(self):
        if self.input_resource_lines:
            return self.name + " needs resource(s) : " + ", ".join(str(i.resource.name) + "=>" + str(i.quantity) for i in self.input_resource_lines)
        else:
            return self.name + " needs no resource"