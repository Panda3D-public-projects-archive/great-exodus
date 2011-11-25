'''
Created on 18 nov. 2011

@author: JD219546
'''
from game_engine.serialization.XML_tools import XML_tools
from game_engine.factories.GalaxyFactory import GalaxyFactory
from game_engine.factories.StarSystemFactory import StarSystemFactory
from game_engine.factories.StarSystemSectorFactory import StarSystemSectorFactory
from game_engine.game_objects.spaceships.ShipProperties import ShipProperties
from game_engine.factories.ShipFactory import ShipFactory
from game_engine.game_objects.database.ShipsDatabase import ShipsDatabase
from game_engine.displacement.Coordinates import Coordinates

class UniverseSerialization(object):
    '''
    classdocs
    '''
    def __call__(self):
        return self

    def __init__(self):
        '''
        Constructor
        '''
        
    def load_universe(self, xml_file):
        xml_tree = XML_tools.get_xml_tree(xml_file)
        galaxies = xml_tree.findall("Galaxy")
        for galaxy in galaxies:
            galaxy_name = galaxy.get("name")
            print "Galaxy :",galaxy_name
            created_galaxy = GalaxyFactory.create_galaxy(galaxy_name)
            star_systems = galaxy.findall("StarSystem")
            for star_system in star_systems:
                star_system_name = star_system.get("name")
                print "\tStarSystem",star_system_name
                created_star_system = StarSystemFactory.create_star_system(created_galaxy, star_system_name)
                star_system_sectors = star_system.findall("StarSystemSector")
                for sector in star_system_sectors:
                    sector_name = sector.get("name")
                    print "\t\tSector",sector_name
                    created_sector = StarSystemSectorFactory.create_star_system_sector(created_star_system, sector_name)
                    ships = sector.findall("Ship")
                    for ship in ships:
                        ship_name = ship.get("name")
                        ship_type = ship.get("type")
                        print "\t\t\tShip",ship_type,ship_name                        
                        ship_properties = ShipsDatabase.get_ship_info_from_type(ship_type)
                        coord = ship.find("Coordinates")
                        ship_coordinate_x = int(coord.get("X"))
                        ship_coordinate_y = int(coord.get("Y"))
                        ship_coordinate_z = int(coord.get("Z"))
                        coordinates = Coordinates(ship_coordinate_x, ship_coordinate_y, ship_coordinate_z)
                        ship_current_speed_ratio = float(ship.get("current_speed"))
                        ship_current_hull_ratio = float(ship.get("current_hull"))
                        ship_properties.current_hull = ship_current_hull_ratio
                        ship_properties.current_speed_ratio = ship_current_speed_ratio
                        ShipFactory.create_ship( ship_name, coordinates, created_sector, ship_properties)
        '''
        galaxies = XML_tools.get_elements_list_from_xml_file(xml_file)
        for galaxy in galaxies:
            name = galaxy.get("name")
            GalaxyFactory.create_galaxy(name)
        '''
        
UniverseSerialization = UniverseSerialization()