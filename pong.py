import pygame
import random

#define variables for game

FPS = 60 

#size of our window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

#size of our paddle 
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

#size of our ball
BALL_WIDTH = 10
BALL_HEIGHT = 10

#speed of our paddle & ball
PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

#RGB Colors paddle and ball
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) #background

#initialize our screen
screen = pygame.display.set_Node(WINDOW_WIDTH,WINDOW_HEIGHT)



def drawBall(ballXpos, ballYPos):
	ball = pygame.rect(ballXpos, ballYPos, BALL_WIDTH, BALL_HEIGHT)
	pygame.draw.rect(screen,WHITE,ball)


def drawPaddle1(paddle1YPos):

	paddle1=pygame.rect(PADDLE_BUFFER,paddle1YPos, PADDLE_WIDTH,PADDLE_HEIGHT)
	pygame.draw.rect(screen, WHITE, paddle1)


def drawPaddle2(paddle2YPos):

	paddle2 = pygame.rect(WINDOW_WIDTH - PADDLE_BUFFER, paddle2YPos,PADDLE_WIDTH,PADDLE_HEIGHT)
	pygame.draw.rect(screen, WHITE, paddle2)







