'''
Created on 4 nov. 2011

@author: JD219546
'''
from controller.Controller import Controller
from game_engine.factories.StarSystemSectorFactory import StarSystemSectorFactory
from game_engine.factories.ShipFactory import ShipFactory

if __name__ == '__main__':
    nb_galaxies = 10
    nb_star_systems_per_galaxy = 10
    nb_star_system_sectors_per_star_system = 10
    nb_ships_per_sector = 30 # There will be one ship of each kind : Fast or Slow    
    contr = Controller()
    contr.create_universe(nb_galaxies, nb_star_systems_per_galaxy, nb_star_system_sectors_per_star_system, nb_ships_per_sector)
    launch_game = 1
    if launch_game:
        star_system_sector = StarSystemSectorFactory.star_systems_sectors_list[0]
        print("Player star system sector = ",star_system_sector.name)
        print("star_system_sector = ",star_system_sector)
        contr.set_player_position_in_universe(star_system_sector)
        contr.display_universe()
        contr.create_initial_movement_lists()
    
        print("Displaying only 10 first spaceships")
    
        contr.start_main_loop()
        print("There was " + str(ShipFactory.number_of_ships()) + " ships to move")
    
    pass