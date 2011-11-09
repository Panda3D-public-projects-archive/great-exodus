'''
Created on 9 nov. 2011

@author: JD219546
'''
from random import randint

class MovementManager(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def move_ship_random(self, ship):
        deltax = randint(-1,1)
        deltay = randint(-1,1)
        deltaz = 0
        ship_coord = ship.get_coordinates()
        newx = deltax + ship_coord.get_x()
        newy = deltay + ship_coord.get_y()
        newz = deltaz + ship_coord.get_z()
        ship.go_to_x_y_z(newx, newy, newz)