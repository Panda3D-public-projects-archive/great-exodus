'''
Created on 13 nov. 2011

@author: JD219546
'''
from game_engine.displacement.MovementManager import MovementManager

class GameStatus(object):
    '''
    classdocs
    '''

    def __call__(self):
        return self

    def __init__(self):
        '''
        Constructor
        '''
        self.iteration = 0
        self.subiteration = 0
        self.subiterations = 0
        self.actually_move = True
    
    def move_to_next_iteration(self, subiterations):
        self.iteration += 1
        self.subiteration = self.iteration % subiterations
        self.actually_move = True
        print("Approximate moves to do : ",self.actually_move)
        
    def subiteration_corresponds(self, counter):
        return counter % self.subiterations == self.subiteration
        
GameStatus = GameStatus()