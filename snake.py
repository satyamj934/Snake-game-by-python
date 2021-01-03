# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 13:00:36 2021

@author: LENOVO
"""
import pygame
from pygame.locals import *
import sys

import random

green=(0,255,255)
red=(255,0,0)
SCREENX=600
SCREENY=600
FPS = 30

pygame.init()
screen=pygame.display.set_mode((SCREENX,SCREENY))
pygame.display.set_caption('snake')
pygame.display.update()
clock=pygame.time.Clock()

font=pygame.font.SysFont(None,30)
background=pygame.image.load('snakebackground.jpg').convert_alpha()

pygame.mixer.init()

def screen_score(text,colour,coordinate):
    screen_text=font.render(text, True, colour)
    screen.blit(screen_text,coordinate)
    
def plot_snake(screen,colour,snk_list,size):
    for x,y in snk_list:
        pygame.draw.rect(screen, green,(x,y,size,size))
        
        
    
def welcome_screen():
    exit_game=False
    while not exit_game:
        screen.blit(background,(0,0))
        screen_score('Welcome To Snake Mayhem', (0,255,255),  (int(SCREENX/5)+50,int(SCREENY/3)))
        screen_score('Press Spacebar to Play', (0,255,255),  (int(SCREENX/5)+50,int(SCREENY/3)+50))
        screen_score('Developed by Satyam jaiswal', (0,255,255),  (int(SCREENX/4),570))
        
        
        
    
    
        for event in pygame.event.get():
                    
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                exit_game=True
            elif event.type==KEYDOWN and event.key==K_SPACE:
                main_game()
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()  
        
    
    
    
def main_game():
    
    px=50
    py=50
    vx=5
    vy=0
    th=8 #threshold for food collision
    score=0
    foodx=random.randint(20,int(SCREENX)/1.5)
    foody=random.randint(20,int(SCREENY)/1.5)
    p_size=10
    snake_length=1
    snk_list=[]
    exit_game=False
    game_over=False
    while not exit_game:
        if game_over:
            
            screen.blit(background,(0,0))
            screen_score('Game Over! press enter to restart', red, (int(SCREENX/3),int(SCREENY/2)))
            for event in pygame.event.get():
                
                if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    exit_game=True
                elif event.type==KEYDOWN and event.key==K_RETURN:
                    main_game()
        else:    
            for event in pygame.event.get():
                
                if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    exit_game=True
                if event.type==KEYDOWN and event.key==K_RIGHT:
                    vx=5
                    vy=0
                if event.type==KEYDOWN and event.key==K_LEFT:
                    vx=-5
                    vy=0
                if event.type==KEYDOWN and event.key==K_UP:
                    vy=-5
                    vx=0
                if event.type==KEYDOWN and event.key==K_DOWN:
                    vy=5
                    vx=0
            px=px+vx
            py=py+vy
            
            if abs(px-foodx)<th and abs(py-foody)<th:
                score+=1
                snake_length+=1
                pygame.mixer.music.load('sound1.mp3')
                pygame.mixer.music.play()
                foodx=random.randint(20,int(SCREENX)/1.5)
                foody=random.randint(20,int(SCREENY)/1.5)
                
            
            snk_list.append([px,py])
            if len(snk_list)>snake_length:
                del snk_list[0]
            if px>SCREENX or py>SCREENY or px<0 or py<0 or ([px,py] in snk_list[:-1]):
                game_over=True
            
            screen.blit(background,(0,0))
            screen_score('Score:'+str(score), red, (5,5))
            plot_snake(screen, green, snk_list, p_size)
            pygame.draw.rect(screen, red,(foodx,foody,p_size,p_size))
    
        pygame.display.update()
        clock.tick(FPS)
    
   
welcome_screen()
