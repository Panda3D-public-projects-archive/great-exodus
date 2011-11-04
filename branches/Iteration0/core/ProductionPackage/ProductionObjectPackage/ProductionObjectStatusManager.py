'''
Created on 22 avr. 2011

@author: JD219546
'''
from core.ProductionPackage.ProductionObjectPackage.ProductionObjectStatusFactory import ProductionObjectStatusFactory

class ProductionObjectStatusManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.production_object_status_factory = ProductionObjectStatusFactory()
        pass
    
    def create_production_object_status(self, resource_to_produce, production_timer_factory):
        self.production_object_status_factory.create_production_status(resource_to_produce, production_timer_factory)