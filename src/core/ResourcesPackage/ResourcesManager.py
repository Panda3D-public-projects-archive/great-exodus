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
        self.food = self.create_resource("food",input_resource_lines = [ResourceNeed(self.ice,2),ResourceNeed(self.ore)])
        self.steel = self.create_resource("steel",2,[ResourceNeed(self.ore,3),ResourceNeed(self.gaz)])
        self.chip = self.create_resource("electronic chip",2, [ResourceNeed(self.crystal,3),ResourceNeed(self.gaz)])
        self.fuel = self.create_resource("fuel",4, [ResourceNeed(self.gaz,5),])
        self.radar = self.create_resource("radar", 1, [ResourceNeed(self.crystal), ResourceNeed(self.chip,3)])
        self.shield_generator = self.create_resource("shield generator", 1, [ResourceNeed(self.crystal, 5), ResourceNeed(self.chip,3)])
        self.engine = self.create_resource("engine", 1, [ResourceNeed(self.steel, 4), ResourceNeed(self.chip)])
        self.hull = self.create_resource("hull", 1, [ResourceNeed(self.steel, 10),])
        self.life_support = self.create_resource("life support", 1, [ResourceNeed(self.food, 2), ResourceNeed(self.gaz,3), ResourceNeed(self.chip)])
                
    def create_resource(self, resource_name, prod_quantity = 1, input_resource_lines = []):
        res = Resource(resource_name, prod_quantity, input_resource_lines)
        self.add_resource_to_list(res)
        return res
    
    def add_resource_to_list(self, resource):
        self.resource_list.append(resource)