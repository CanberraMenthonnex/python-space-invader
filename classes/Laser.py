import pygame 
from classes.Collision import Collision

class Laser: 
    def __init__(self,x,y):
        self.size = 5
        self.vel = 5
        self.X = x
        self.Y = y 

    def SpawnMoveUp(self, ecran):
        self.Y-= self.vel
        pygame.draw.circle(ecran, (0,123,0), (self.X,self.Y), self.size)
    
    def SpawnMoveDown(self, ecran):
        self.Y+= self.vel
        pygame.draw.circle(ecran, (0,123,0), (self.X,self.Y), self.size)
    


