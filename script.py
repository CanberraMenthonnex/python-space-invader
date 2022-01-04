import pygame
from random import randint
from classes.Spaceship import Spaceship
from classes.Collision import Collision
from classes.Alien import Alien

module_charge = pygame.init()

ecran = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invader By Canberra")
pygame.mixer.music.load("music.mp3")
pygame.mixer.init()
pygame.mixer.music.play(-1)
bg = pygame.image.load("bg.jpeg")

game = True
loop = True
font = pygame.font.SysFont("Consolas", 40)


spaceship = Spaceship()
aliens1 = []
alien = Alien()
lp = 1

while lp < 8:
    alien = Alien()
    alien.X = lp * 100
    aliens1.append(alien)
    lp += 1
i = 0
while game:

    if loop == False:
        print(i)
        i +=1
        ecran.blit(bg, (0, 0))
        font.render("GAME OVER", True,(0,0,0))
        pygame.display.update()
        

    elif loop:
        ecran.blit(bg, (0, 0))
          
        if aliens1: 
            for t in aliens1:
                t.Spawn(ecran)
                t.Shoot(ecran)

                if t.Y > 580:
                    loop = False

                for laser in t.shoots:
                    if((((laser.X - spaceship.X)**2) + ((laser.Y - spaceship.Y)**2) )**0.5) < 30:
                        loop = False

                #collision
                for laser in spaceship.shoots:
                    if ((((laser.X - t.X)**2) + ((laser.Y - t.Y)**2) )**0.5) < 30:
                        aliens1.remove(t)

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
        pygame.display.update()

pygame.quit()
