import pygame
import time
import random
pygame.init()

WHITE=(255, 255, 255)
YELLOW= (255, 255, 102)
BLACK=(0, 0, 0)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLUE=(0, 0, 255)

W=800
H=600

sc=pygame.display.set_mode((W, H))

clock=pygame.time.Clock()

snake_block=10
snake_speed=15

font_style=pygame.font.SysFont("bahnschrift", 100)
score_font=pygame.font.SysFont("bahnschrift", 25)
 
def Your_score(score):
    value=score_font.render("Your score: "+str(score), True, WHITE)
    sc.blit(value, [0, 0])
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(sc, GREEN, [x[0], x[1], snake_block, snake_block])
 
def message(msg, color):
    mesg=font_style.render(msg, True, color)
    sc.blit(mesg, [W/5.5, H/2.5])
 
def gameLoop():
    game_over=False
    game_close=False
    x1=W/2
    y1=H/2
    x1_change=0
    y1_change=0
    snake_List=[]
    Length_of_snake=1
    foodx=round(random.randrange(0, W-snake_block)/10.0)*10.0
    foody=round(random.randrange(0, H-snake_block)/10.0)*10.0

    while not game_over:
        while game_close==True:
            sc.fill(BLACK)
            message("Game Over", RED)
            Your_score(Length_of_snake-1)
            pygame.display.update()
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                elif event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                elif event.key==pygame.K_UP:
                    y1_change=-snake_block
                    x1_change=0
                elif event.key==pygame.K_DOWN:
                    y1_change=snake_block
                    x1_change=0
        if x1>=W or x1<0 or y1>=H or y1<0:
            game_close=True
        x1+=x1_change
        y1+=y1_change
        sc.fill(BLACK)
        pygame.draw.rect(sc, RED, [foodx, foody, snake_block, snake_block])
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List)>Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x==snake_Head:
                game_close=True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake-1)
        pygame.display.update()
        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0, W-snake_block)/10.0)*10.0
            foody=round(random.randrange(0, H-snake_block)/10.0)*10.0
            Length_of_snake+=1
        clock.tick(snake_speed)
        
gameLoop()