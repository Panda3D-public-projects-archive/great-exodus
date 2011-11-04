'''
Created on 22 avr. 2011

@author: JD219546
'''

class ProductionState(object):
    '''
    classdocs
    '''

    def __init__(self, production_status):
        '''
        Constructor
        '''
        self.production_status = production_status
        pass
    
    def evolve_state(self):
        raise Exception("IMPLEMENT evolve_state in UNDERLYING SUBCLASS")
        pass
    
    def produce(self, production_rule, stock):
        raise Exception("IMPLEMENT produce in UNDERLYING SUBCLASS")
        pass        