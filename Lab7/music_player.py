import pygame
pygame.init()

W, H=800, 600

screen=pygame.display.set_mode((W, H))

sound=[
    pygame.mixer.Sound('1.mp3'),
    pygame.mixer.Sound('2.mp3'),
    pygame.mixer.Sound('3.mp3')
]

cnt=0

font=pygame.font.SysFont('arial', 45)

playmusic=font.render("Press Space to play music", True, (231, 84, 128))
stopmusic=font.render("Press Enter to play music", True, (231, 84, 128))
nextmusic=font.render("Press D to play next music", True, (231, 84, 128))
previousmusic=font.render("Press A to play previous music", True, (231, 84, 128))
upvolume=font.render("Press W to add sound", True, (231, 84, 128))
downvolume=font.render("Press S to turn down the sound", True, (231, 84, 128))

play=False
vol=1

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and not play:
                play=True
                sound[cnt].play()

            elif event.key == pygame.K_RETURN:
                play=False
                sound[cnt].stop()

            elif event.key==pygame.K_d:
                play=True
                sound[cnt].stop()
                cnt+=1
                if cnt>=len(sound):
                    cnt=0
                sound[cnt].play()

            elif event.key==pygame.K_a:
                play=True
                sound[cnt].stop()
                cnt-=1
                if cnt<0:
                    cnt=len(sound)-1
                sound[cnt].play()

            elif event.key==pygame.K_s:
                vol-=0.1
                sound[cnt].set_volume(vol)
                print(sound[cnt].get_volume())

            elif event.key==pygame.K_w:
                vol+=0.1
                sound[cnt].set_volume(vol)
                print(sound[cnt].get_volume())

    screen.fill((250, 245, 218))     
    screen.blit(playmusic, (100, 30))
    screen.blit(stopmusic, (100, 130))
    screen.blit(nextmusic, (100, 230))
    screen.blit(previousmusic, (100, 330))
    screen.blit(upvolume, (100, 430))
    screen.blit(downvolume, (100, 530))
    
    pygame.display.update()