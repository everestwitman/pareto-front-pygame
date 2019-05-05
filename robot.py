import pygame 
from pygame.locals import *

import constants as c
import random

class Robot:
    def __init__(self, index, position): 
        self.index = index
        self.position = position
        self.color = c.colorRGBsPygame[index]    
    
    def getX(self):
        return self.position[0]
        
    def getY(self):
        return self.position[1]
        
    def setX(self, x): 
        self.position = (x, self.getY())
        
    def setY(self, y): 
        self.position = (self.getY(), y)
        
    def moveUp(self, distance): 
        self.setY(self.getY() + distance)
        
    def moveDown(self, distance): 
        self.setY(self.getY() - distance)
    
    def moveRight(self, distance): 
        self.setX(self.getX() + distance)
    
    def moveLeft(self, distance): 
        self.setX(self.getX() - distance)
            
        
    # For translating coordinates with origin in bottom left
    # to coordinates with origins in top left for Pygame drawing
    def translate_position(self, position):
        translated_position = (position[0], c.DISPLAY_HEIGHT - position[1])
        return translated_position
        
    def drawPoint(self, surface, markerSize):
        pygame.draw.circle(surface, self.color, self.translate_position(self.position), markerSize)
    
    def drawShadow(self, surface):
        translated_position = self.translate_position(self.position)
        pygame.draw.rect(surface, c.BLACK, (translated_position[0], translated_position[1], c.DISPLAY_WIDTH - translated_position[0], c.DISPLAY_HEIGHT - translated_position[1]))
    
    def inShadow(self, pop):         
        for bot in pop:
            if bot.getX() < self.getX() and bot.getY() > self.getY(): 
                return True 
        return False 
