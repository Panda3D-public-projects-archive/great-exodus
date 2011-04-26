'''
Created on 19 avr. 2011

@author: JD219546
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, quantity_to_produce, needed_resource_dict, time_interval):
        '''
        Constructor
        '''
        self.quantity_to_produce = quantity_to_produce
        self.needed_resources = needed_resource_dict
        self.production_time_interval = time_interval
        
        
        