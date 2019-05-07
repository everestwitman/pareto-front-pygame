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
        
        self.paretoFront = []
        self.dominatedBots = []
        self.updateParetoFront()
        
        self.primaryBotId= self.randomPrimaryBotId()
        
        self.clock = pygame.time.Clock()
        pygame.init()
        
    
    def draw(self): 
        display = pygame.display.set_mode((c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT))
        pygame.display.set_caption('Pareto Front')
        
        runForever = True
        while runForever: 
            # Listen for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    runForever = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.pop[self.primaryBotId].moveLeft(10)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.pop[self.primaryBotId].moveRight(10)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.pop[self.primaryBotId].moveUp(10)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.pop[self.primaryBotId].moveDown(10)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.paretoFront[-1].dying = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.paretoFront[-1].dying = True        
                        
            

            # Update values 
            self.updateParetoFront()
            self.animateMovement()
            self.clearDead()
            
            # Redraw shadow and bots
            display.fill(c.WHITE)    
            self.drawShadow(display)
            self.drawPoints(display, self.primaryBotId)
            
            # Pygame cycle updates 
            pygame.display.update()
            self.clock.tick(60)
    
    def randomPrimaryBotId(self):     
        return self.paretoFront[random.randint(0, len(self.paretoFront) - 1)].id
    
    # Mutates paretoFront and dominatedBots
    def updateParetoFront(self): 
        self.paretoFront = []
        self.dominatedBots = []
        for bot in self.pop: 
            if not(bot.inShadow(self.pop)):
                self.paretoFront.append(bot)
            else:
                self.dominatedBots.append(bot)
        
        for bot in self.paretoFront:
            bot.revive()
        
        for bot in self.dominatedBots: 
            bot.die()
    
    def animateMovement(self): 
        for bot in self.pop:
            bot.moveAnimationFrame()
    
    def drawPoints(self, surface, primaryBotId):    
        for bot in self.pop:
            if (bot.id != primaryBotId):
                bot.draw(surface, c.MARKER_SIZE)
            else:
                bot.draw(surface, c.PRIMARY_MARKER_SIZE)
    
    def clearDead(self):
        for i in range(0, len(self.pop)):
            if i < len(self.pop):
                if (self.pop[i].dying == True) and (self.pop[i].animation_countdown == 0) and (self.pop[i].getX() < 0) and (self.pop[i].getY() < 0):
                    print("clearDead")
                    del self.pop[i]
                    print(len(self.pop))

    def drawShadow(self, surface):
        for bot in self.paretoFront: 
            if bot.dying == False:
                bot.drawShadow(surface)
         
paretoFront = ParetoFront()
paretoFront.draw()
