import pygame

class player():
    def __init__(self, screen, color, x, y, width, height, speed):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.offset = 5
        self.screenHeight = screen.get_height()
        self.screenWidth = screen.get_width()

    # draw the enemy on screen
    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    # increase the y position of the enemy
    def increaseYPos(self):
        if (self.screenHeight - self.y - self.height - self.offset > 0):
            self.y += self.speed
            return True
        return False

    # decrease the y position of the enemy
    def decreaseYPos(self):
        if (self.y - self.offset > 0):
            self.y -= self.speed
            return True
        return False

    # get the y position of the enemy
    def getYPos(self):
        return self.y
    
    # increase the X position of the enemy
    def increaseXPos(self):
        self.x += self.speed

    # decrease the x position of the enemy
    def decreaseXPos(self):
        self.x -= self.speed

    # get the x position of the enemy
    def getXPos(self):
        return self.x

    # get the width of the player
    def getWidth(self):
        return self.width
    
    # get the height of the player
    def getHeight(self):
        return self.height

    # follows the direction of the ball
    def followBall(self, ball):
        # gets the top and bottom of the player
        a = self.y
        b = self.y + self.height

        # gets the current positon of the ball
        y = ball.getYPos()

        # checks if the ball's positon is less than the top of the ball
        if (y < a):
            self.decreaseYPos()
        # checks if the ball's positon if greater than the bottom of the
        if (y > b):
           self.increaseYPos()