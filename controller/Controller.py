'''
Created on 4 nov. 2011

@author: JD219546
'''
from game_engine.GameEngine import GameEngine
from gui.Gui import Gui
from time import sleep
from time import clock

class Controller(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.game_engine = GameEngine()
        self.gui = Gui()
        self.max_iterations = 10
        self.main_clock = float(1)/ 5
        self.main_loop_iterations = 0
        
    def start_main_loop(self):
        start_ = clock()
        while True:
            st = clock()
            self.game_engine.update(self.main_loop_iterations)
            self.gui.update()
            iteration_time = clock() - st
            if iteration_time < self.main_clock:
                sleep_time = self.main_clock - iteration_time
            else:
                sleep_time = 0
            self.main_loop_iterations += 1
            print("Iteration : ",self.main_loop_iterations," main_clock = ",self.main_clock," iteration time = ",iteration_time," and sleep time : ",sleep_time)
            sleep(sleep_time)
            
            if self.main_loop_iterations == self.max_iterations:
                break
            
            
        end_ = clock()
        print("Execution time = ",end_-start_," and expected : ",self.max_iterations*self.main_clock)