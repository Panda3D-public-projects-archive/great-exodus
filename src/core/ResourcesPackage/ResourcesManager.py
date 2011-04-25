# -*- coding: latin-1 -*-
'''
Created on 25 févr. 2011

@author: goungy
'''
from core.ResourcesPackage.ResourceNeed import ResourceNeed
from core.ResourcesPackage.Resource import Resource


class ResourcesManager(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''      
        self.resource_list = []
        
        self.ice = self.create_resource("ice")
        self.ore = self.create_resource("ore")
        self.gaz = self.create_resource("gaz")
        self.crystal = self.create_resource("crystal")
        self.food = self.create_resource("food")
        self.steel = self.create_resource("steel")
        self.chip = self.create_resource("electronic chip")
        self.fuel = self.create_resource("fuel")
        self.radar = self.create_resource("radar")
        self.shield_generator = self.create_resource("shield generator")
        self.engine = self.create_resource("engine")
        self.hull = self.create_resource("hull")
        self.life_support = self.create_resource("life support")
                
    def create_resource(self, resource_name, prod_quantity = 1, input_resource_lines = {}):
        res = Resource(resource_name, prod_quantity, input_resource_lines)
        self.add_resource_to_list(res)
        return res
    
    def add_resource_to_list(self, resource):
        self.resource_list.append(resource)