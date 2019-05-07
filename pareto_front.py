import pygame 
from pygame.locals import *
from robot import Robot
import constants as c
import random


class ParetoFront:
    def __init__(self):     
        self.pop = []
        for i in range(0, c.popSize): 
            self.pop.append(Robot(i, (random.randint(0, c.DISPLAY_WIDTH), random.randint(0, c.DISPLAY_HEIGHT))))
        
        self.paretoFront = self.calculateParetoFront()
        self.primaryBotIndex = self.randomPrimaryBotIndex()
        
        # print(self.paretoFront[0].color)
        # self.paretoFront[0].animateMovementToPos((50,50), 100)
        
        self.clock = pygame.time.Clock()
        pygame.init()
        
    
    def draw(self): 
        display = pygame.display.set_mode((c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT))
        pygame.display.set_caption('Pareto Front')
        
        runForever = True
        while runForever: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runForever = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.pop[self.primaryBotIndex].moveLeft(10)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.pop[self.primaryBotIndex].moveRight(10)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.pop[self.primaryBotIndex].moveUp(10)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.pop[self.primaryBotIndex].moveDown(10)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.paretoFront[-1].dying = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.paretoFront[-1].dying = True
                    
            display.fill(c.WHITE)
            
            # self.animateMovement()
            self.drawShadow(display)
            self.drawPoints(display, self.primaryBotIndex)
            self.updateParetoFront()
            pygame.display.update()
            self.clock.tick(60)
    
    def randomPrimaryBotIndex(self):     
        return self.paretoFront[random.randint(0, len(self.paretoFront) - 1)].index
        
    def updateParetoFront(self): 
        self.paretoFront = self.calculateParetoFront()
        
    def calculateParetoFront(self):
        paretoFront = []
        for bot in self.pop: 
            if not(bot.inShadow(self.pop)):
                paretoFront.append(bot)
                bot.revive()
            else:
                bot.die()
                
        return paretoFront
    
    def animateMovement(self): 
        for bot in self.pop:
            bot.moveAnimationFrame()
    
    def drawPoints(self, surface, primaryBotIndex):    
        for bot in self.pop:
            # self.clearDead()
            if (bot.index != primaryBotIndex):
                bot.moveAnimationFrame(surface, c.MARKER_SIZE)
            else:
                bot.moveAnimationFrame(surface, c.PRIMARY_MARKER_SIZE)
    
    def clearDead(self):
        for bot in self.pop:
            if (bot.dying == True) and (bot.animation_countdown == 0):
                "clearDead"
                del bot

    def drawShadow(self, surface):
        for bot in self.paretoFront: 
            bot.drawShadow(surface)
         
paretoFront = ParetoFront()
paretoFront.draw()
