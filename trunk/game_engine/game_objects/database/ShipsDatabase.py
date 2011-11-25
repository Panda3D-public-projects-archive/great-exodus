'''
Created on 17 nov. 2011

@author: JD219546
'''

from xml.etree import ElementTree as ET
import os
from game_engine.game_objects.spaceships.ShipProperties import ShipProperties

class ShipsDatabase(object):
    '''
    classdocs
    '''
    def __call__(self):
        return self

    def __init__(self, xml_file = "game_engine/game_objects/database/ships.xml"):
        '''
        Constructor
        '''
        self.ships_dict_by_type = {}
        self.add_ships_from_file(xml_file)
        
    def get_ships_types(self):
        return self.ships_dict_by_type.items()
        
    def add_ships_from_file(self, xml_file):
        print "ShipsDatabase CWD = ",os.getcwd()
        tree = ET.parse(xml_file)
        ships = tree.findall("*")
        for ship in ships:
            max_speed = float(ship.get("speed"))
            max_hull = float(ship.get("hull"))
            print ship.tag,"max speed:",max_speed,"max hull:",max_hull
            self.ships_dict_by_type[ship.tag] = ShipProperties(ship.tag, max_speed , max_hull)
                            
    def get_ship_info_from_type(self, ship_type_name):
        return  self.ships_dict_by_type[ship_type_name]
           
ShipsDatabase = ShipsDatabase() 