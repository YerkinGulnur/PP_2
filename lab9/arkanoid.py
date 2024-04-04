import pygame 
import random

pygame.init()

W, H = 800, 600
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (255, 192, 203)

# Paddle
paddleW = 200
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Blocks
block_width = 100
block_height = 50
blocks = [{'rect': pygame.Rect(10 + 120 * i, 50 + 70 * j, block_width, block_height),
           'color': (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)),
           'hits': 1, 'destroyed': False, 'indestructible': False}
          for i in range(10) for j in range(4)]

# Make some blocks indestructible
indestructible_blocks = random.sample(blocks, 5)  # Choose 5 blocks randomly
for block in indestructible_blocks:
    block['indestructible'] = True

# Sound
collision_sound = pygame.mixer.Sound('catch.mp3')

# Game over
font = pygame.font.SysFont('comicsansms', 40)
text = font.render('Game Over', True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (W // 2, H // 2)

# Main menu
def main_menu():
    menu_font = pygame.font.SysFont('comicsansms', 40)
    start_text = menu_font.render('Start Game (Press Space)', True, (0, 0, 0))
    settings_text = menu_font.render('Settings (Press S)', True, (0, 0, 0))
    screen.blit(start_text, (W // 2 - start_text.get_width() // 2, H // 2 - 50))
    screen.blit(settings_text, (W // 2 - settings_text.get_width() // 2, H // 2 + 50))
    pygame.display.update()

# Settings menu
def settings_menu():
    settings_done = False
    while not settings_done:
        screen.fill(bg)
        font = pygame.font.SysFont('comicsansms', 40)
        paddle_speed_text = font.render(f'Paddle Speed: {paddleSpeed}', True, (0, 0, 0))
        ball_speed_text = font.render(f'Ball Speed: {ballSpeed}', True, (0, 0, 0))
        screen.blit(paddle_speed_text, (W // 2 - paddle_speed_text.get_width() // 2, H // 2 - 50))
        screen.blit(ball_speed_text, (W // 2 - ball_speed_text.get_width() // 2, H // 2 + 50))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings_done = True
                elif event.key == pygame.K_UP:
                    paddle_speed_increase()
                elif event.key == pygame.K_DOWN:
                    paddle_speed_decrease()
                elif event.key == pygame.K_LEFT:
                    ball_speed_decrease()
                elif event.key == pygame.K_RIGHT:
                    ball_speed_increase()
                elif event.key == pygame.K_SPACE:  # Переход к основному циклу игры
                    settings_done = True

def paddle_speed_increase():
    global paddleSpeed
    paddleSpeed += 1

def paddle_speed_decrease():
    global paddleSpeed
    paddleSpeed -= 1

def ball_speed_increase():
    global ballSpeed
    ballSpeed += 1

def ball_speed_decrease():
    global ballSpeed
    ballSpeed -= 1

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Start game
                main_loop = True
                while main_loop:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            main_loop = False
                            done = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                main_loop = False
                            if event.key == pygame.K_p:  # Pause
                                paused = True
                                while paused:
                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_p:
                                                paused = False
                                    screen.fill(bg)
                                    font = pygame.font.SysFont('comicsansms', 40)
                                    paused_text = font.render('Paused', True, (0, 0, 0))
                                    screen.blit(paused_text, (W // 2 - paused_text.get_width() // 2, H // 2))
                                    pygame.display.update()
                            if event.key == pygame.K_s:  # Settings
                                settings_menu()
                    screen.fill(bg)
                    # Draw paddle and ball
                    pygame.draw.rect(screen, pygame.Color(234, 250, 177), paddle)
                    pygame.draw.circle(screen, pygame.Color(250, 241, 157), ball.center, ballRadius)
                    # Paddle Control
                    key = pygame.key.get_pressed()
                    if key[pygame.K_LEFT] and paddle.left > 0:
                        paddle.left -= paddleSpeed
                    if key[pygame.K_RIGHT] and paddle.right < W:
                        paddle.right += paddleSpeed
                    # Ball movement
                    ball.x += ballSpeed * dx
                    ball.y += ballSpeed * dy
                    # Collision with walls
                    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
                        dx = -dx
                    if ball.centery < ballRadius + 50:
                        dy = -dy
                    # Collision with paddle
                    if ball.colliderect(paddle) and dy > 0:
                        dy = -dy
                    # Collision with blocks
                    for block in blocks:
                        if block['hits'] > 0 and ball.colliderect(block['rect']):
                            if not block['indestructible']:  # Check if the block is destructible
                                dy = -dy
                                block['hits'] -= 1
                                if block['hits'] == 0:
                                    block['destroyed'] = True
                            else:
                                dx = -dx
                                dy = -dy
                            collision_sound.play()
                    # Draw blocks
                    for block in blocks:
                        if not block['destroyed']:
                            pygame.draw.rect(screen, block['color'], block['rect'])
                    # Check if all blocks are destroyed
                    if all(block['destroyed'] for block in blocks):
                        screen.fill((255, 255, 255))
                        screen.blit(text, textRect)
                    # Check if ball is out of bounds
                    if ball.y > H or ball.x > W:
                        screen.fill((0, 0, 0))
                        screen.blit(text, textRect)
                    # Update game objects
                    pygame.display.update()
                    clock.tick(FPS)
            elif event.key == pygame.K_s:  # Settings
                settings_menu()
                    
    screen.fill(bg)
    main_menu()
    pygame.display.flip()

pygame.quit()
