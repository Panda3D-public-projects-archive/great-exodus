'''
Created on 22 avr. 2011

@author: JD219546
'''
from core.ProductionPackage.ProductionStatePackage.ProductionState import ProductionState


class ProductionStateInitial(ProductionState):
    '''
    classdocs
    '''

    """
    def __init__(self, production_status):
        '''
        Constructor
        '''
        self.production_status = production_status
        pass
    """
    
    def evolve_state(self, production_object, enough_input_resources, enough_room, iteration):
        if enough_input_resources:
            if enough_room:
                #everything's alright
                self.production_status.set_state_to_producing()
            else:
                #missing room
                self.production_status.set_state_to_wait_room()
        else:
            #not enough input resources, but maybe enough room
            if enough_room:
                #enough room but not resources
                self.production_status.set_state_to_wait_resource()
            else:
                #not enough anything: remain in the same state
                pass
    
    def produce(self, production_object):
        pass
    
    def __str__(self):
        return "InitialProductionState"