'''
Created on 22 avr. 2011

@author: JD219546
'''
from core.ProductionPackage.ProductionRule import ProductionRule
from core.ProductionPackage.ProductionNeed import ProductionNeed
from core.ProductionPackage.ProductionLine import ProductionLine

class ProductionRuleFactory(object):
    '''
    classdocs
    '''

    def create_small_factory_production_rule(self, resource, production_timer_factory, input_resources= [], quantity = 1):
        
        self.create_production_rule("small "+resource.name+" factory",
                                    [resource, ],
                                    [production_timer_factory.get_production_timer(resource), ],
                                    [input_resources, ],
                                    [quantity,])

    def __init__(self, resource_manager, production_timer_factory):
        '''
        Constructor
        '''
        self.production_rules_map = {}
        self.create_production_rule("small planet", 
                                    [resource_manager.ore, resource_manager.ice], 
                                    [production_timer_factory.get_production_timer(resource_manager.ore), 
                                     production_timer_factory.get_production_timer(resource_manager.ice)],
                                    [[], []],
                                    [1, 1])
        self.create_small_factory_production_rule(resource_manager.ore, production_timer_factory)
        self.create_small_factory_production_rule(resource_manager.ice, production_timer_factory)
        self.create_small_factory_production_rule(resource_manager.gaz, production_timer_factory)
        self.create_small_factory_production_rule(resource_manager.crystal, production_timer_factory)
        self.create_small_factory_production_rule(resource_manager.food, production_timer_factory, 
                                                  [ProductionNeed(resource_manager.ice,2), ProductionNeed(resource_manager.ore)])
        self.create_small_factory_production_rule(resource_manager.steel, production_timer_factory, 
                                                  [ProductionNeed(resource_manager.ore,3), ProductionNeed(resource_manager.gaz)],
                                                  2) 
        self.create_small_factory_production_rule(resource_manager.chip, production_timer_factory, 
                                                  [ProductionNeed(resource_manager.crystal,3), ProductionNeed(resource_manager.gaz)],
                                                  2)
        self.create_small_factory_production_rule(resource_manager.fuel, production_timer_factory, 
                                                  [ ProductionNeed(resource_manager.gaz,5),],
                                                  4)
        self.create_small_factory_production_rule(resource_manager.radar, production_timer_factory, 
                                                  [ProductionNeed(resource_manager.crystal), ProductionNeed(resource_manager.chip,3)])
        self.create_small_factory_production_rule(resource_manager.shield_generator, production_timer_factory, 
                                                  [ProductionNeed(resource_manager.crystal,5), ProductionNeed(resource_manager.chip,3)])
        self.create_small_factory_production_rule(resource_manager.engine, production_timer_factory, 
                                                  [ProductionNeed(resource_manager.steel,4), ProductionNeed(resource_manager.chip)])
        self.create_small_factory_production_rule(resource_manager.hull, production_timer_factory, 
                                                  [ProductionNeed(resource_manager.steel,10),])
        self.create_small_factory_production_rule(resource_manager.life_support, production_timer_factory, 
                                                  [ProductionNeed(resource_manager.food,2), ProductionNeed(resource_manager.gaz,3), ProductionNeed(resource_manager.chip)])
        pass
    
    def create_production_rule(self, identifier, items_to_produce, production_times, resources_needed, quantities):
        #print("Creating production rule "+identifier)
        production_rule = ProductionRule()
        for i in range(len(items_to_produce)):
            production_rule.check_and_add_production_line(items_to_produce[i], ProductionLine(resources_needed[i],production_times[i],quantities[i]))
#        production_rule = ProductionRule(resources_needed, items_to_produce, production_times, quantities)
        self.add_production_rule(identifier,production_rule)
        
    def add_production_rule(self, identifier, production_rule):
        self.production_rules_map[identifier] = production_rule
        
    def get_all_production_rules_map(self):
        return self.production_rules_map
    
    def get_production_rule(self, identifier):
        return self.production_rules_map[identifier]