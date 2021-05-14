import pygame
import time
import random
import sys
import os

# Pygame window initialization
pygame.init()
clock=pygame.time.Clock()

#Colour Declaration
orangecolor=(255,123,7)
blackcolor=(0,0,0)
redcolor=(213,50,80)
greencolor=(0,255,0)
bluecolor=(50,153,213)

#Display screen size

display_width=600
display_height=400
display=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Snake Game")

snake_block=10
snake_speed=50
snake_list=[]

# Define snake structure and position
def Snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(display,orangecolor,[x[0],x[1],snake_block,snake_block])

def SnakeGame():
    gameover=False
    gameend=False

    #Cordinate of Snake
    x1=display_width/2
    y1=display_height/2

    #When snake move
    x1_change = 0
    y1_change = 0

    #length of snake
    length_of_sanke=1
    #Cordinate of food
    foodx=round(random.randrange(0,display_width - snake_block)/10.0) * 10.0
    foody=round(random.randrange(0,display_height - snake_block)/10.0) * 10.0

    while not gameover:
        while gameend==True:
            display.fill(bluecolor)
            font_style=pygame.font.SysFont("comicsansms",15)
            message=font_style.render("Game Lost \n Press P for restart",True,redcolor)
            display.blit(message,[display_width /6,display_height/3])

            score=length_of_sanke -1
            score_font=pygame.font.SysFont("comicsansms",25)
            value=score_font.render("Your Score " + str(score),True, greencolor)
            display.blit(value,[display_width / 3,display_height/5])

            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_p:
                        SnakeGame()
                if event.type ==pygame.QUIT:
                    gameover=True
                    gameend=False
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameover=True
            
            if event.type ==pygame.KEYDOWN:
                if event.key ==pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change=0
                elif event.key == pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key== pygame.K_UP:
                    y1_change= -snake_block
                    x1_change =0
                elif event.key == pygame.K_DOWN:
                    y1_change= snake_block
                    x1_change =0
                
        if x1 >= display_width or x1 <0 or y1 >=display_height or y1<0:
            gameend=True

        #Update cordinate
        x1 += x1_change
        y1 += y1_change
        display.fill(blackcolor)
        pygame.draw.rect(display,greencolor,[foodx,foody,snake_block,snake_block])

        sanke_head=[]
        sanke_head.append(x1)
        sanke_head.append(y1)
        snake_list.append(sanke_head) 

        if len(snake_list) > length_of_sanke:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x==sanke_head:
                gameend=True
        
        Snake(snake_block,snake_list)
        pygame.display.update()

        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0,display_width - snake_block) /10.0) * 10.0
            foody=round(random.randrange(0,display_height - snake_block) /10.0) * 10.0
            length_of_sanke += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()
SnakeGame()