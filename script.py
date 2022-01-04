import pygame
import time
from classes.Spaceship import Spaceship
from classes.Collision import Collision
from classes.Alien import Alien

module_charge = pygame.init()

ecran = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invader 3000")

loop = True
invaderAlive = True

aliens = []

alien = Alien()
aliens.append(alien)

spaceship = Spaceship()


while loop:
    ecran.fill((0,0,0))

    try:
        alien
    except:
        pass
    else:
        alien.Spawn(ecran)
        alien.Shoot(ecran)
        #die 
        if alien.Y > 480:
            loop = False

        for laser in alien.shoots:
            if( (((laser.X - spaceship.X)**2) + ((laser.Y - spaceship.Y)**2) )**0.5) < 30:
                loop = False
        #collision
        for laser in spaceship.shoots:
            if ((((laser.X - alien.X)**2) + ((laser.Y - alien.Y)**2) )**0.5) < 30:
                del alien 
        

    for t in aliens:
        
        

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                loop = False
            if event.key == pygame.K_q:
                spaceship.move = "left"
            if event.key == pygame.K_d:
                spaceship.move = "right"
            if event.key == pygame.K_SPACE:
                spaceship.Shoot(ecran)

        if event.type == pygame.QUIT:
            loop = False
     

    spaceship.Move(ecran)
    spaceship.Spawn(ecran)
    pygame.display.flip()
    # time.sleep(0.025)


pygame.quit()
