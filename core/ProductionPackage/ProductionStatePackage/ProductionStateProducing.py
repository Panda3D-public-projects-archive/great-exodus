'''
Created on 22 avr. 2011

@author: JD219546
'''
from core.ProductionPackage.ProductionStatePackage.ProductionState import ProductionState

class ProductionStateProducing(ProductionState):
    '''
    classdocs
    '''

    """
    def __init__(self):
        '''
        Constructor
        '''
        pass
    """
    
    def evolve_state(self, production_object, enough_input_resources, enough_room, iteration):
        if enough_input_resources:
            if enough_room:
                #everything's alright
                pass
            else:
                #missing room
                self.production_status.set_state_to_wait_room()
        else:
            #not enough input resources, but maybe enough room
            if enough_room:
                #enough room but not resources
                self.production_status.set_state_to_wait_resource()
            else:
                #not enough anything
                self.production_status.set_state_to_initial()
                pass
        
    def produce(self, production_object):
        production_object.produce()
        
    def __str__(self):
        return "ProducingProductionState"
        