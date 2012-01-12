'''
Created on 9 nov. 2011

@author: JD219546
'''
from random import randint

class MovementManager(object):
    '''
    classdocs
    '''
    move_approximately_ship_every_X_iterations = 4
    move_accurately_ship_every_iterations = 100

    def __call__(self):
        return self

    def __init__(self):
        '''
        Constructor
        '''
        self.accurate_movement_sector = None      
                
    def update_movement_lists(self, new_sector):
        self.accurate_movement_sector = new_sector
        pass
    
    def move_ships_in_sector_random_accurately(self):
        self.accurate_movement_sector.move_ships_random_accurately()

    def move_ship_random_accurately(self, ship):
        #print("MovementManager moving ships accurately")
        self.move_ship_random(ship, self.move_accurately_ship_every_iterations)
        
    def move_ship_random_approximately(self, ship):
        #print("MovementManager moving ships approximately")
        self.move_ship_random(ship, self.move_approximately_ship_every_X_iterations)

        
    def move_ships_random(self, ships, speed_modifier = 1):
        for ship in ships:
            self.move_ship_random(ship)
        
    def move_ships_random_accurately(self, ships):
        #print("MovementManager moving ships accurately")
        self.move_ships_random(ships, self.move_accurately_ship_every_iterations)
        
    def move_ships_random_approximately(self, ships):
        #print("MovementManager moving ships approximately")
        self.move_ships_random(ships, self.move_approximately_ship_every_X_iterations)
    
    def move_ship_random(self, ship, speed_modifier = 1):
        deltax = randint(-1,1) * speed_modifier
        deltay = randint(-1,1) * speed_modifier
        deltaz = 0 * speed_modifier
        ship_coord = ship.get_coordinates()
        newx = deltax * ship.speed + ship_coord.get_x()
        newy = deltay * ship.speed+ ship_coord.get_y()
        newz = deltaz * ship.speed+ ship_coord.get_z()
        ship.go_to_x_y_z(newx, newy, newz) 
        
MovementManager = MovementManager()
