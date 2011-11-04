'''
Created on 8 avr. 2011

@author: JD219546
'''

class ProductionTimerFactory(object):
    '''
    classdocs
    '''


    def __init__(self, resource_manager):
        '''
        Constructor
        '''
        #defining intervals
        self.time_interval_dict = {}
        self.time_interval_dict[resource_manager.food] = 3
        self.time_interval_dict[resource_manager.crystal] = 3
        self.time_interval_dict[resource_manager.gaz] = 3        
        self.time_interval_dict[resource_manager.chip] = 3
        self.time_interval_dict[resource_manager.fuel] = 2
        self.time_interval_dict[resource_manager.ice] = 1
        self.time_interval_dict[resource_manager.ore] = 1
        self.time_interval_dict[resource_manager.steel] = 8
        self.time_interval_dict[resource_manager.radar] = 3
        self.time_interval_dict[resource_manager.shield_generator] = 3
        self.time_interval_dict[resource_manager.engine] = 3
        self.time_interval_dict[resource_manager.hull] = 2
        self.time_interval_dict[resource_manager.life_support] = 2
        

    def get_production_timer(self, resource):
        return self.time_interval_dict[resource]

    
        