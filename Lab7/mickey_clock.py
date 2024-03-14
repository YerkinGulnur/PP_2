import pygame
import datetime
pygame.init()

W, H=800, 800

sc=pygame.display.set_mode((W, H))

x=W//2
y=H//2

WHITE=(255, 255, 255)

clock=pygame.time.Clock()

mickey=pygame.image.load('main-clock.png')
rightHand=pygame.image.load('right-hand.png')
leftHand=pygame.image.load('left-hand.png')

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    
    date=datetime.datetime.now()
    sec=date.second
    min=date.minute

    rotated_min=pygame.transform.rotate(rightHand, -50-(min*6))
    rotated_min_rect=rotated_min.get_rect(center=(x, y))

    rotated_sec=pygame.transform.rotate(leftHand, -(6*sec))
    rotated_sec_rect=rotated_sec.get_rect(center=(x, y))

    sc.blit(mickey, (0, 0))
    sc.blit(rotated_min, rotated_min_rect)
    sc.blit(rotated_sec, rotated_sec_rect)

    pygame.display.update()
    clock.tick(60)
    