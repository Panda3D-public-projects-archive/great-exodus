'''
Created on 10 nov. 2011

@author: jerome
'''

class GameObject(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name