'''
Created on 9 nov. 2011

@author: JD219546
'''
from game_engine.displacement.Spaceship import Spaceship
from game_engine.displacement.Coordinates import Coordinates

class ShipFactory(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.ship_list = []
        
    def create_ship(self, name = None, coordinates = Coordinates(0, 0, 0)):
        if not name:
            name = "spaceship"+str(self.number_of_ships())            
        ship = Spaceship(name, coordinates)
        #print(ship)
        self.ship_list.append(ship)
        
    def get_ship_list(self):
        return self.ship_list
        
    def number_of_ships(self):
        return len(self.ship_list)