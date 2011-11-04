'''
Created on 20 avr. 2011

@author: JD219546
'''
import time

class ControllerTimer(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.time_tick = float(1)/float(25)
        #print("time tick = ",self.time_tick,"s")
        self.overall_start = None
        self.current_time = None
        
    def start(self):
        self.overall_start = time.time()
        self.current_time = time.time()    
        
    def wait(self):
        temp_current_time = time.time()
        remaining_wait_time = self.time_tick - self.current_time + temp_current_time
        if remaining_wait_time > 0:
            remaining_wait_time = min(remaining_wait_time,self.time_tick)
            time.sleep(remaining_wait_time)
        self.current_time = time.time()
        