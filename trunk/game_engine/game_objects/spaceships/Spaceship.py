'''
Created on 8 nov. 2011

@author: benjamin
'''
from game_engine.game_objects.MovableSpaceObject import MovableSpaceObject


"""
We need to take into account the fact that every spaceship has a speed. It therefore can not go instantly at a given coordinates.
In order to simplify the model, we will "jump" to the coordinates expected.
"""

class Spaceship(MovableSpaceObject):

    def __init__(self, name, coordinates, star_system_sector, speed):
        super(Spaceship, self).__init__(name, coordinates, star_system_sector, speed)
        
        



        