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
        
    def Spawn(self, ecran):
        pygame.draw.circle(ecran, (255,0,0), (self.X,self.Y), self.size)
        self.Y += self.vel
        self.pos += 1

        for items in self.shoots:
            items.SpawnMoveDown(ecran)

    def Shoot(self, ecran):
        roll = randrange(100)
        if roll == 1:
            laser = Laser(self.X, self.Y)
            self.shoots.append(laser)
            
    
