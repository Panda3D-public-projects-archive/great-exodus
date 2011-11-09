'''
Created on 4 nov. 2011

@author: JD219546
'''
from controller.Controller import Controller

if __name__ == '__main__':
    contr = Controller()
    contr.game_engine.create_ships(1000)
    print("Displaying only 10 first spaceships")
    contr.start_main_loop()
    
    pass