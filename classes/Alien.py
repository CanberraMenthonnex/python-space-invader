import pygame
from random import randrange
from classes.Laser import Laser


class Alien:
    def __init__(self):
        self.X = 400
        self.Y = 0
        self.size = 20
        self.vel = 0.25
        self.pos = 0
        self.aliens = []
        self.shoots = []
        self.spaceshipImg = pygame.image.load("ufo.png")
        
    def Spawn(self, ecran):
        ecran.blit(self.spaceshipImg, (self.X, self.Y))
        self.Y += self.vel
        self.pos += 1

        for items in self.shoots:
            items.SpawnMoveDown(ecran)

    def MoveLeft(self):
        self.X -= self.vel * 3

    def MoveRight(self):
        self.X += self.vel * 3

    def Shoot(self, ecran):
        roll = randrange(150)
        if roll == 1:
            laser = Laser(self.X, self.Y)
            self.shoots.append(laser)
            
    
