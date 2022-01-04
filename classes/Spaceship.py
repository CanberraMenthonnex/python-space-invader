import pygame
from classes.Laser import Laser

class Spaceship():
    def __init__(self):
        self.X = 400
        self.Y = 500
        self.size = 20
        self.vel = 2 
        self.move = "null"
        self.shoots = []

    def Spawn(self, ecran):
        pygame.draw.circle(ecran, (0,0,255), (self.X,self.Y), self.size)

    def Move(self, ecran):
        if self.move == "left":
            self.X = self.X - self.vel
        elif self.move == "right":
            self.X = self.X + self.vel
        for items in self.shoots:
            items.SpawnMoveUp(ecran)

    def Shoot(self, ecran):
        laser = Laser(self.X, self.Y)
        self.shoots.append(laser)