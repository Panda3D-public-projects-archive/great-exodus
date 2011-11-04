'''
Created on 25 avr. 2011

@author: JD219546
'''

class ProductionNeed(object):
    '''
    classdocs
    '''


    def __init__(self, resource, quantity=1):
        '''
        Constructor
        '''
        self.resource = resource
        self.quantity = quantity
        