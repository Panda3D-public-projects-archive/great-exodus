'''
Created on 4 nov. 2011

@author: JD219546
'''
from controller.Controller import Controller
from game_engine.factories.GalaxyFactory import GalaxyFactory
from game_engine.factories.StarSystemFactory import StarSystemFactory
from game_engine.factories.StarSystemSectorFactory import StarSystemSectorFactory
from game_engine.game_objects.spaceships.Spaceship import Spaceship
from game_engine.factories.ShipFactory import ShipFactory

if __name__ == '__main__':
    nb_ships_per_sector = 4 # There will be one ship of each kind : Fast or Slow
    nb_galaxies = 5
    nb_star_systems_per_galaxy = 10
    nb_star_system_sectors_per_star_system = 10
    contr = Controller()
    contr.game_engine.create_galaxies(nb_galaxies)
    for galaxy in GalaxyFactory.galaxies_list:
        contr.game_engine.create_star_systems(galaxy, nb_star_systems_per_galaxy)
        for star_system in StarSystemFactory.star_systems_dict[galaxy]:
            contr.game_engine.create_star_system_sectors(star_system, nb_star_system_sectors_per_star_system)
            for star_system_sector in StarSystemSectorFactory.star_systems_sectors_dict[star_system]:
                contr.game_engine.create_ships_in_star_system_sector(star_system_sector, nb_ships_per_sector)
                
    for galaxy in GalaxyFactory.galaxies_list:
        print("GGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
        galaxy.print_star_systems()
        for star_system in StarSystemFactory.star_systems_dict[galaxy]:
            print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
            star_system.print_star_system_sectors()
            for star_system_sector in StarSystemSectorFactory.star_systems_sectors_dict[star_system]:
                #star_system_sector.print_spaceships()
                pass
    print("Displaying only 10 first spaceships")

    contr.start_main_loop()
    print("There was " + str(ShipFactory.number_of_ships()) + " ships to move")
    pass