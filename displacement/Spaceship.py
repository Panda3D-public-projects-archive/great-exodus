'''
Created on 8 nov. 2011

@author: benjamin
'''

from trunk.displacement.Coordinates import Coordinates

"""
We need to take into account the fact that every spaceship has a speed. It therefore can not go instantly at a given coordinates.
In order to simplify the model, we will "jump" to the coordinates expected.
"""

class Spaceship:

    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates

    def __print__(self):
        return 'Name :', self.name, 'Coordinates :', self.coordinates

    def get_name(self):
        return self.name

    def get_coordinates(self):
        return self.coordinates

    def set_name(self, name):
        self.name = name

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def go_to_coord(self, coordinates):
        self.go_to_x_y_z(coordinates.get_x(), coordinates.get_y(), coordinates.get_z())
    
    def go_to_x_y_z(self, x, y, z):
        self.set_coordinates(Coordinates(x, y, z))   

        