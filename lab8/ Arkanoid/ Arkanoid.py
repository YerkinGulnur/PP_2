import pygame 
import random

pygame.init()

W, H = 800, 600
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (255, 192, 203)

paddleW = 200
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

#Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')


# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game over
font = pygame.font.SysFont('comicsansms', 40)
text = font.render('Game Over', True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (W // 2, H // 2)

# Variables for upgrades
start_time = pygame.time.get_ticks()
speed_increase_interval = 30000  # Increase speed every 30 seconds
speed_increase_amount = 1
paddle_shrink_interval = 60000  # Shrink paddle every 60 seconds
paddle_shrink_amount = 20  # Amount to shrink paddle width
block_hit_increase_interval = 20000  # Increase the number of hits needed to destroy blocks every 20 seconds
block_hit_increase_amount = 1

# Blocks
block_width = 100
block_height = 50
blocks = [{'rect': pygame.Rect(10 + 120 * i, 50 + 70 * j, block_width, block_height),
           'color': (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)),
           'hits': 1, 'destroyed': False, 'indestructible': False}  # Add 'indestructible' attribute
          for i in range(10) for j in range(4)]

# Make some blocks indestructible
indestructible_blocks = random.sample(blocks, 5)  # Choose 5 blocks randomly
for block in indestructible_blocks:
    block['indestructible'] = True

# Game over screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

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
        screen.blit(wintext, wintextRect)

    # Check if ball is out of bounds
    if ball.y > H or ball.x > W:
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)

    # Update game objects
    pygame.display.update()
    clock.tick(FPS)

    # Apply upgrades over time
    current_time = pygame.time.get_ticks()
    if current_time - start_time > speed_increase_interval:
        ballSpeed += speed_increase_amount
        start_time = current_time

    if current_time - start_time > paddle_shrink_interval:
        paddleW -= paddle_shrink_amount
        paddle.width = paddleW
        start_time = current_time

    if current_time - start_time > block_hit_increase_interval:
        for block in blocks:
            block['hits'] += block_hit_increase_amount
        start_time = current_time