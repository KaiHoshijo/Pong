import pygame
import random

class ball():
    def __init__(self, screen, color, center, radius, speed):
        self.screen = screen
        self.color = color
        self.center = center
        self.centerList = list(center)
        self.radius = radius
        self.speed = speed
        self.screenHeight = screen.get_height()
        self.screenWidth = screen.get_width()
        self.moveRight = random.randint(0, 1)
        # self.moveRight = 0
        self.moveDown = random.randint(0, 1)
        self.xSpeed = random.uniform(.5, 1.0)
        self.ySpeed = random.uniform(.5, 1.0)
        # self.ySpeed = 0
        self.alive = True

    # draw the ball onto the screen
    def draw(self):
        if (self.alive):
            self.center = tuple(self.centerList)
            pygame.draw.circle(self.screen, self.color, self.center, self.radius)

    # increase the y position of the ball
    def increaseYPos(self):
        if (self.screenHeight - self.centerList[1] - self.radius > 0):
            self.centerList[1] += round(self.speed * self.ySpeed)
            return True
        return False
    
    # decrease the y position of the ball
    def decreaseYPos(self):
        if (self.centerList[1] - self.radius > 0): 
            self.centerList[1] -= round(self.speed * self.ySpeed)
            return True
        return False

    # get the y position of the ball
    def getYPos(self):
        return self.centerList[1]

    # increase the x position of the ball
    def increaseXPos(self):
        if (self.screenWidth - self.centerList[0] - self.radius > 0):
            self.centerList[0] += round(self.speed * self.xSpeed)
            return True
        # self.alive = False
        return False
    
    # decrease the x position of the ball
    def decreaseXPos(self):
        if (self.centerList[0] - self.radius > 0): 
            self.centerList[0] -= round(self.speed * self.xSpeed)
            return True
        # self.alive = False
        return False

    # get the x position of the ball
    def getXPos(self):
        return self.centerList[0]

    # generate new x speed
    def newXSpeed(self, a):
        self.xSpeed = random.uniform(1.0, a)
    
    # generate new y speed
    def newYSpeed(self, a):
        self.ySpeed = random.uniform(1.0, a)

    # get the radius
    def getRadius(self):
        return self.radius

    # start motion of the game
    def move(self):
        # move right or left
        if (self.moveRight == 1):
            if (not self.increaseXPos()):
                self.moveRight = 0
                self.newXSpeed(2.0)
        else:
            if (not self.decreaseXPos()):
                self.moveRight = 1
                self.newXSpeed(2.0)
        # move up or down
        if (self.moveDown == 1):
            if (not self.increaseYPos()):
                self.moveDown = 0
                self.newYSpeed(2.0)
        else:
            if (not self.decreaseYPos()):
                self.moveDown = 1
                self.newYSpeed(2.0)
    
    # bounce off of player
    def bounce(self, player, enemy = False):
        # width requirements
        a = player.getXPos()
        b = player.getXPos() + player.getWidth()
        # height requirements
        c = player.getYPos() 
        d = player.getYPos() + player.getHeight()

        # circle positions
        xs = [self.getXPos() - self.radius, self.getXPos() + self.radius]
        y = self.getYPos()

        if (xs[0] in range(a, b+1) or xs[1] in range(a, b+1)):
            # print("X")
            if (y in range(c, d+1)):
                if (enemy):
                    self.moveRight = 0
                    self.newXSpeed(2.0)
                    self.newYSpeed(2.0)
                else:
                    self.moveRight = 1
                    self.newXSpeed(2.0)
                    self.newYSpeed(2.0)
        
