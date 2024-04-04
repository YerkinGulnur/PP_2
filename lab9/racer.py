import pygame
import random
import time
pygame.init()

pygame.display.set_caption('Game')

W=400
H=600
 
sc=pygame.display.set_mode((W, H))

BLUE=(0, 0, 255)
RED=(255, 0, 0)
GREEN=(0, 255, 0)
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
 
sc.fill(WHITE)

clock=pygame.time.Clock()

SPEED=5
SCORE=0
SCORE1=0

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

font=pygame.font.SysFont("Verdana", 60)
font_small=pygame.font.SysFont("Verdana", 20)
game_over=font.render("Game Over", True, BLACK)
 
background=pygame.image.load("AnimatedStreet.png")
 
sc=pygame.display.set_mode((W, H))
sc.fill(WHITE)
 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image=pygame.image.load("Enemy.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40, W-40), 0)  
 
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top>600):
            SCORE+=1
            self.rect.top=0
            self.rect.center=(random.randint(40, W-40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Coin.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40, W-40), 0)  
        self.image.set_colorkey((WHITE))

    def move(self):
        global SCORE1
        self.rect.move_ip(0, SPEED)
        if(self.rect.bottom>600):
            self.rect.top=0
            self.rect.center=(random.randint(40, W-40), 0)
        elif Collide():
            SCORE1+=1
            self.rect.top=0
            self.rect.center=(random.randint(self.rect.width, H-self.rect.width), 0) 

class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Coin2.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40, W-40), 0)  
        self.image.set_colorkey((WHITE))

    def move(self):
        global SCORE1
        self.rect.move_ip(0, SPEED)
        if(self.rect.bottom>1000):
            self.rect.top=0
            self.rect.center=(random.randint(40, W-40), 0)
        elif Collide2(): 
            SCORE1+=3
            self.rect.top=0
            self.rect.center=(random.randint(self.rect.width, H-self.rect.width), 0) 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image=pygame.image.load("Player.png")
        self.rect=self.image.get_rect()
        self.rect.center=(160, 520)
        
    def move(self):
        pressed_keys=pygame.key.get_pressed()  
        if self.rect.left>0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right<W:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)
                           
P1=Player()
E1=Enemy()
C1=Coin()
C2=Coin2()

enemies=pygame.sprite.Group()
enemies.add(E1)
coins=pygame.sprite.Group()
coins.add(C1)
coins2=pygame.sprite.Group()
coins2.add(C2)
all_sprites=pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)
 
INC_SPEED=pygame.USEREVENT+1
pygame.time.set_timer(INC_SPEED, 1000)

def Collide():
    if pygame.sprite.spritecollideany(P1, coins):
        return True
    else:
        return False

def Collide2():
    if pygame.sprite.spritecollideany(P1, coins2):
        return True
    else:
        return False

while True:
    for event in pygame.event.get():
        if event.type==INC_SPEED:
            SPEED+=0.5     
        if event.type==pygame.QUIT:
            exit()
 
    sc.blit(background, (0, 0))
    scores=font_small.render(str(SCORE), True, BLACK)
    sc.blit(scores, (10, 10))
    
    scores1=font_small.render(str(SCORE1), True, BLACK)
    sc.blit(scores1, (370, 10))

    for entity in all_sprites:
        sc.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(C1, enemies):
        C1.rect.center=(random.randint(40, W-40), 0)

    if pygame.sprite.spritecollideany(C1, coins2):
        C1.rect.center=(random.randint(40, W-40), 0)

    if pygame.sprite.spritecollideany(C2, enemies):
        C2.rect.center=(random.randint(40, W-40), 0)

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
                    
        sc.fill(RED)
        sc.blit(game_over, (30,250))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
            time.sleep(0.5)
        exit()

    pygame.display.update()
    clock.tick(60)