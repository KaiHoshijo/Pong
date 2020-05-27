import pygame 
from pygame.locals import *
import random

import Player
import Ball

# initialize the model
pygame.init()

# set up the canvas
screen = pygame.display.set_mode((500, 500))
# get the clock of the canvas
clock = pygame.time.Clock()
# name of the game
pygame.display.set_caption("Pong")
# creating the background for the canvas
background = pygame.Surface(screen.get_size())
# font for the game
font = pygame.font.Font(None, 36)

# size of screen
screenWidth = screen.get_width()
screenHeight = screen.get_height()
print(screenWidth, screenHeight)

# speed of the player and the enemy
speed = 3

# enemy's X
enemyX = 450

# player's X
playerX = 50

# players' width and height
playerWidth = 10
playerHeight = 50

# players' Y
playerY = screenHeight // 2 - playerHeight // 2

#players' color
playerColour = (245, 245, 245)

# bounce for the enemy
moveDown = True

# constant moving for the player
moveY = 0

# player score
playerScore = 0
# enemy score
enemyScore = 0

# Ball's colour
ballColour = (255, 255, 255)

# Ball's initial location
ballCenter = (screenWidth // 2, screenHeight // 2)

# Ball's radius
ballRadius = 8

# Ball's speed
ballSpeed = 2

# setting up the enemy
enemy = Player.player(screen, playerColour, enemyX, playerY, playerWidth, playerHeight, speed)
# setting up the player
player = Player.player(screen, playerColour, playerX, playerY, playerWidth, playerHeight, speed*2)

# setting up the ball
ball = Ball.ball(screen, ballColour, ballCenter, ballRadius, ballSpeed)

play = True
while play:
    # filling the screen
    screen.fill((23, 23, 23))

    # writing the score of the game
    text = font.render("{}   {}".format(playerScore, enemyScore), 1, (255, 255, 255))
    textpos = text.get_rect(centerx=screen.get_width()/2)
    screen.blit(text, textpos)

    for event in pygame.event.get():
        if (event.type == QUIT):
            play = False
        elif (event.type == KEYDOWN):
            if (event.key == K_UP): 
                # enemy.increaseXPos()
                moveY = -1
            elif (event.key == K_DOWN):
                # enemy.decreaseXPos()
                moveY = 1
        elif (event.type == KEYUP):
            if (event.key == K_UP or event.key == K_DOWN):
                moveY = 0
        
    # move the player
    if (moveY == 1):
        player.increaseYPos()
    elif (moveY == -1):
        player.decreaseYPos()



    # updating enemy position
    enemy.followBall(ball)

    if (moveDown):
        if (not enemy.increaseYPos()):
            moveDown = False
    else:
        if (not enemy.decreaseYPos()):
            moveDown = True

    # updating ball position
    ball.move()
    # follow the ball
    player.followBall(ball)
    # bounce the ball
    ball.bounce(player)
    ball.bounce(enemy, enemy=True)
    # drawing the ball
    ball.draw()
    # drawing the enemy
    enemy.draw()
    # drawing the player
    player.draw()

    # update the score
    if (ball.getXPos() < player.getXPos()):
        enemyScore += 1
        # setting up the enemy
        enemy = Player.player(screen, playerColour, enemyX, playerY, playerWidth, playerHeight, speed)
        # setting up the player
        player = Player.player(screen, playerColour, playerX, playerY, playerWidth, playerHeight, speed)
        # setting up the ball
        ball = Ball.ball(screen, ballColour, ballCenter, ballRadius, ballSpeed)
    elif (ball.getXPos() > enemy.getXPos()):
        playerScore += 1
        # setting up the enemy
        enemy = Player.player(screen, playerColour, enemyX, playerY, playerWidth, playerHeight, speed)
        # setting up the player
        player = Player.player(screen, playerColour, playerX, playerY, playerWidth, playerHeight, speed)
        # setting up the ball
        ball = Ball.ball(screen, ballColour, ballCenter, ballRadius, ballSpeed)
    
    # updating the background
    # screen.blit(background, (0, 0))
    pygame.display.flip()

    # setting the frame rate
    clock.tick(60)