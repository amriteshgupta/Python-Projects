# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 22:09:09 2020

@author: prave
"""

import pygame,sys,random

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,668))
    screen.blit(floor_surface, (floor_x_pos+432,668))
    
def create_pipe():
    new_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(440,new_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(440,new_pipe_pos-300))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx-=3
    return pipes
    
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom>=768:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe, pipe)
            
def check_coll(pipes):
    for pipe in pipes:
        if bird_rect.colliderect((pipe)):
            death_sound.play()
            return False
            
    if bird_rect.top<=0 or bird_rect.bottom>=668: 
        return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement*6, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100,bird_rect.centery))
    return new_bird,new_bird_rect

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render("Score: "+str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center=(215,80))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render("Score: "+str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center=(215,80))
        screen.blit(score_surface, score_rect)
        
        high_score_surface = game_font.render("High Score: "+str(int(high_score)),True,(255,255,255))
        high_score_rect = high_score_surface.get_rect(center=(218,630))
        screen.blit(high_score_surface, high_score_rect)
        
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1,buffer=256)
pygame.init()

screen = pygame.display.set_mode((432,768))
clock  = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf', 30)

#Game variables
gravity = 0.025
bird_movement = 0
game_active = True
score = 0
high_score = 0

message_surface = pygame.transform.scale(pygame.image.load("Images/message.png").convert_alpha(),(276,400))
message_surface_rect = message_surface.get_rect(center=(215,350))

flap_sound = pygame.mixer.Sound('Sounds/sfx_wing.wav')
death_sound = pygame.mixer.Sound('Sounds/sfx_hit.wav')
score_sound = pygame.mixer.Sound('Sounds/sfx_point.wav')
#score_countdown=1000

bg_surface = pygame.image.load('Images/background-night.png').convert()
bg_surface = pygame.transform.scale(bg_surface,(432,768) )

floor_surface = pygame.image.load('Images/base.png').convert()
floor_surface = pygame.transform.scale(floor_surface, (432,100))
floor_x_pos = 0

bird_downflap = pygame.transform.scale(pygame.image.load('Images/redbird-downflap.png'). convert_alpha(),(51,36))
bird_midflap = pygame.transform.scale(pygame.image.load('Images/redbird-midflap.png'). convert_alpha(),(51,36))
bird_upflap = pygame.transform.scale(pygame.image.load('Images/redbird-upflap.png'). convert_alpha(),(51,36))
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100,384))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)


#bird_surface = pygame.image.load('Images/redbird-midflap.png'). convert_alpha()
#bird_surface = pygame.transform.scale(bird_surface,(51,36))
#bird_rect = bird_surface.get_rect(center=(100,384))

pipe_surface = pygame.image.load('Images/pipe-red.png')
pipe_surface = pygame.transform.scale(pipe_surface, (78,480))
pipe_list=[]
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [400,500,600]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement=0
                bird_movement-=2
                flap_sound.play()
                
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center =(100,384)
                bird_movement=0
                score = 0
            
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
            
        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
                
            bird_surface,bird_rect = bird_animation()
            
    screen.blit(bg_surface, (0,0))
  
    if game_active:
        #Bird
        bird_movement+=gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery+=bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_coll(pipe_list)
    
        #pipe
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        
        score+=.01
        #score_countdown-=1
        score_display('main_game')
        #if (score_countdown <= 0):
           # score_sound.play()
            
        
    else:
        if score > high_score:
            high_score=score
        score_display('game_over')
        screen.blit(message_surface, message_surface_rect)
    
    #Floor
    floor_x_pos-=1
    draw_floor()
    if floor_x_pos<=-432:
        floor_x_pos=0
    
    
    pygame.display.update() 
    clock.tick(120)