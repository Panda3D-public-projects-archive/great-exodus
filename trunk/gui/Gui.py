'''
Created on 4 nov. 2011

@author: JD219546
'''
from direct.showbase.ShowBase import ShowBase

class Gui(ShowBase):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        ShowBase.__init__(self)
        pass
        
    
    def update(self):
        print "Updating GUI"
        self.taskMgr.step()
        pass