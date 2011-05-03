# By Coincoin
# Created : 22 March 2011
# Modified : 22 March 2011

import pygame
import random

from pygame.locals import *


def CreateList(n):

    tab = list(range(n))
    for i in range(len(tab)) :
        tab[i] = random.randint(0, 20)

    return tab


def RefreshDisplay(win, ship, backgrnd, pos_ship, bullet, pos_bullet) :

    win.blit(backgrnd, (0,0))
    win.blit(ship, pos_ship)
    win.blit(bullet, pos_bullet)
    pygame.display.flip()


def LaunchGame(win, ship, backgrnd, pos_ship, bullet, pos_bullet) :

    pygame.key.set_repeat(400, 30)
    ship_speed = 4
    fire = False

    pos_bullet = pos_ship.move(24, -10)

    running = True


    while running :
    
        pygame.time.Clock().tick(30)        # Frame/s

        for event in pygame.event.get() :    # Check any end signal
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN :
                if event.key == K_DOWN :
                    pos_ship = pos_ship.move(0, ship_speed)
                if event.key == K_UP :
                    pos_ship = pos_ship.move(0, -ship_speed)
                if event.key == K_LEFT :
                    pos_ship = pos_ship.move(-ship_speed, 0)
                if event.key == K_RIGHT :
                    pos_ship = pos_ship.move(ship_speed, 0)
                # TODO : 2 keys pressed do not work with key.set_repeat
                if event.key == K_LEFT and event.key == K_DOWN :
                    pos_ship = pos_ship.move(-ship_speed, ship_speed)
                if event.key == K_RIGHT and event.key == K_DOWN :
                    pos_ship = pos_ship.move(ship_speed, ship_speed)
                if event.key == K_LEFT and event.key == K_UP :
                    pos_ship = pos_ship.move(-ship_speed, -ship_speed)
                if event.key == K_RIGHT and event.key == K_UP  :
                    pos_ship = pos_ship.move(ship_speed, -ship_speed)
                if event.key == K_SPACE :
                    fire = True

        if fire == True :
            pos_bullet = pos_bullet.move(0, -10)
            if pos_bullet.top < 10 :
                fire = False
        else :
            pos_bullet = pos_ship.move(24, -10)

        RefreshDisplay(win, ship, backgrnd, pos_ship, bullet, pos_bullet)


def main():
    
    # Initialize pygame library
    pygame.init()

    pygame.display.set_caption("Canard Space Ship Commander v1.3")

    print("\_o< Welcome on board ! Canard Space Ship TEST !!!!")
    print("Press DOWN, UP, LEFT, RIGHT to move spaceship")
    print("Press SPACE to fire")

    win = pygame.display.set_mode((640, 480))

    # Load and paste background
    backgrnd = pygame.image.load("space.jpg").convert()

    # Load and paste space ship
    ship = pygame.image.load("spaceship.png").convert_alpha()
    pos_ship = ship.get_rect()    # Ship coordinates
    pos_ship = pos_ship.move(320, 420)

    # Load Bullet
    bullet = pygame.image.load("bullet.png").convert_alpha()
    pos_bullet = bullet.get_rect()

    RefreshDisplay(win, ship, backgrnd, pos_ship, bullet, pos_bullet)
    
    LaunchGame(win, ship, backgrnd, pos_ship, bullet, pos_bullet)



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
