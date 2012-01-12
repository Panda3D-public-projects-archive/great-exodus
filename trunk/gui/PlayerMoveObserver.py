'''
Created on 2 dec. 2011

@author: jd219546
'''

class PlayerMoveObserver(object):
    '''
    classdocs
    '''


    def __init__(self, observer, observed):
        '''
        Constructor
        observer is gui.PlayerScene
        observed is PlayerStatus
        '''
        self.observer = observer
        self.observed = observed
        observed.set_player_move_observer(self)
        
    def update_position_in_universe(self, star_system_sector):
        print "PlayerMoveObserver updating : ",star_system_sector.get_name()
        self.observer.get_ships_from_sector(star_system_sector)
    