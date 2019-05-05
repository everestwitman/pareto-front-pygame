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
            
        self.primaryBotIndex = random.randint(0, len(self.pop) - 1)
        
        self.clock = pygame.time.Clock()
        pygame.init()
        
    
    def draw(self): #(self, robots, primaryBotPosition):
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
                    
            display.fill(c.WHITE)

            self.drawShadow(display)
            self.drawPoints(display, self.primaryBotIndex)
            pygame.display.update()
            self.clock.tick(60)
                
    def paretoFront(self):
        paretoFront = []
        for bot in self.pop: 
            if not(bot.inShadow()):
                paretoFront.append(bot)
                
        return paretoFront
                
    
    def drawPoint(self, surface, color, botIndex, markerSize):
        pygame.draw.circle(surface, color, self.botPositions[botIndex], markerSize)
    
    def drawPoints(self, surface, primaryBotIndex):
        if (primaryBotIndex > -1):
            self.pop[primaryBotIndex].drawPoint(surface, 48)

        for bot in self.pop:
            if (bot.index != primaryBotIndex) and not(bot.inShadow(self.pop)):
                bot.drawPoint(surface, 24)
            
        botsInShadow = 0    
        for bot in self.pop:
            if bot.inShadow(self.pop): 
                botsInShadow += 1
        
        print(len(self.pop))
        print(botsInShadow)
        print(self.pop[0].color)
        print(self.pop[0].position)
    
    def drawShadow(self, surface):
        for bot in self.pop: 
            bot.drawShadow(surface)
            
paretoFront = ParetoFront()
paretoFront.draw()
