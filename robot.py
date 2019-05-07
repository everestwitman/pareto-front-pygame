import pygame 
from pygame.locals import *
import pytweening 
import constants as c
import random

class Robot:
    def __init__(self, index, position): 
        self.index = index
        self.position = position
        self.color = c.colorRGBsPygame[index]    
        self.dying = False
        self.velocity = [0, 0]
        self.animation_countdown = 0
        # self.die()
        self.startingAnimation()
    
    def getX(self):
        return self.position[0]
        
    def getY(self):
        return self.position[1]
        
    def setX(self, x): 
        self.position = (x, self.getY())
        
    def setY(self, y): 
        self.position = (self.getX(), y)
        
    def moveAnimationFrame(self): 
        print(self.animation_countdown)
        if self.animation_countdown > 0: 
            # self.setX(self.getX() + pytweening.easeInQuad(self.animation_countdown / c.FPS) * 20)
            # self.setY(self.getY() + pytweening.easeInQuad(self.animation_countdown / c.FPS) * 0)
            self.moveRight(self.velocity[0])
            self.moveUp(self.velocity[1])
            self.animation_countdown -= 1
        else: 
            self.stopMovement()
            if self.dying == True: 
                self.animateMovementToPos((-2 * (c.PRIMARY_MARKER_SIZE), (-2 * (c.PRIMARY_MARKER_SIZE))), 20)
                
        # self.draw(surface, markerSize)
            
    # def moveAnimationFrame(self, surface, markerSize): 
    # 
    #     print(self.animation_countdown)
    #     if self.animation_countdown < 20: 
    #         self.setX(self.getX() + pytweening.easeInQuad(self.animation_countdown / c.FPS) * 20)
    #         self.setY(self.getY() + pytweening.easeInQuad(self.animation_countdown / c.FPS) * 0)
    #         # self.moveRight(self.velocity[0])
    #         # self.moveUp(self.velocity[1])
    #         self.animation_countdown += 1
    # 
    #     self.draw(surface, markerSize)
    # 
    #     # else: 
    #         # self.stopMovement()
    #         # if self.dying == True: 
    #         #     del self
            
    def startingAnimation(self):
        position = self.position
        self.position = (0,0)
        self.animateMovementToPos(position, 20)
    
    # Move bot to position over countdown frames 
    def animateMovementToPos(self, destination, countdown):
        x_dist = destination[0] - self.getX()
        y_dist = destination[1] - self.getY()
        
        x_speed = round(x_dist / countdown)
        y_speed = round(y_dist / countdown)
        
        self.velocity = [x_speed, y_speed]
        self.animation_countdown = countdown
        
    # velocity param is an array 
    # countdown is the number of frames the movement should last
    def animateMovementVel(self, velocity, countdown):
        self.velocity = velocity 
        self.animation_countdown = countdown
        
    def stopMovement(self): 
        self.velocity = (0,0)
        self.animation_countdown = 0
        
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
        translated_position = (int(position[0]), int(c.DISPLAY_HEIGHT - position[1]))
        return translated_position
        
    def draw(self, surface, markerSize):
        # self.moveAnimationFrame()
        pygame.draw.circle(surface, self.color, self.translate_position(self.position), markerSize)
        if self.dying:
            self.drawCrossOfDeath(surface)
    
    def drawShadow(self, surface):
        translated_position = self.translate_position(self.position)
        pygame.draw.rect(surface, c.BLACK, (translated_position[0], translated_position[1], c.DISPLAY_WIDTH - translated_position[0], c.DISPLAY_HEIGHT - translated_position[1]))
    
    def drawCrossOfDeath(self, surface): 
        trans_pos = self.translate_position(self.position)
        pygame.draw.line(surface, c.RED, (trans_pos[0] - c.MARKER_SIZE, trans_pos[1] - c.MARKER_SIZE), (trans_pos[0] + c.MARKER_SIZE, trans_pos[1] + c.MARKER_SIZE), 4) 
        pygame.draw.line(surface, c.RED, (trans_pos[0] - c.MARKER_SIZE, trans_pos[1] + c.MARKER_SIZE), (trans_pos[0] + c.MARKER_SIZE, trans_pos[1] - c.MARKER_SIZE), 4) 
    
    def revive(self):
        self.dying = False
        
    def die(self): 
        print("dying")
        print(self.color)
        self.dying = True
        # self.animation_countdown = 10
        
    def inShadow(self, pop):         
        for bot in pop:
            if bot.getX() < self.getX() and bot.getY() > self.getY(): 
                return True 
        return False 
