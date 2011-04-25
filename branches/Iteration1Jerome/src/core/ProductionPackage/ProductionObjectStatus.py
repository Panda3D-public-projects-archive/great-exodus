'''
Created on 21 avr. 2011

@author: JD219546
'''
from core.ProductionPackage.ProductionStatePackage.ProductionStateInitial import ProductionStateInitial
from core.ProductionPackage.ProductionStatePackage.ProductionStateInsufficientResources import ProductionStateInsufficientResources
from core.ProductionPackage.ProductionStatePackage.ProductionStateInsufficientRoom import ProductionStateInsufficientRoom
from core.ProductionPackage.ProductionStatePackage.ProductionStateProducing import ProductionStateProducing

class ProductionObjectStatus(object):
    '''
    classdocs
    '''

    def __init__(self, previous_iteration):
        '''
        Constructor
        '''
        self.production_state_initial = ProductionStateInitial(self)
        self.production_state_insufficient_resources = ProductionStateInsufficientResources(self)
        self.production_state_insufficient_room = ProductionStateInsufficientRoom(self)
        self.production_state_producing = ProductionStateProducing(self) 
        self.production_state = self.production_state_initial 
        self.previous_iteration = previous_iteration
              
    def evolve_state(self, production_object, enough_input_to_produce, enough_space_to_produce, current_iteration):
        self.production_state.evolve_state(production_object, enough_input_to_produce, enough_space_to_produce, current_iteration)
     
    def produce(self, production_object):
        self.production_state.produce(production_object)
        
    def set_state_to(self, state):
        self.production_state = state
        
    def set_state_to_producing(self):
        self.set_state_to(self.production_state_producing)

    def set_state_to_initial(self):
        self.set_state_to(self.production_state_initial)    
        
    def set_state_to_wait_room(self):
        self.set_state_to(self.production_state_insufficient_room)
        
    def set_state_to_wait_resource(self):
        self.set_state_to(self.production_state_insufficient_resources)
        
                