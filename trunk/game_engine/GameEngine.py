'''
Created on 4 nov. 2011

@author: JD219546
'''
from game_engine.factories.ShipFactory import ShipFactory
from game_engine.displacement.MovementManager import MovementManager

class GameEngine(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.shipfactory = ShipFactory()
        self.movement_manager = MovementManager()
        
    def update(self, iteration_number):
        ship_list = self.shipfactory.get_ship_list()
        i = 0
        for ship in ship_list:
            self.movement_manager.move_ship_random(ship)
            if i < 10 : print(ship)
            i += 1
        pass
    '''
    Help function to create ships for testing.
    Will not be part of final project.
    '''
    def create_ships(self, nb_ships = 0):
        for i in range(nb_ships):
            self.shipfactory.create_ship()