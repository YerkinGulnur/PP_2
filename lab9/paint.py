import pygame
pygame.init()

W = 600
H = 600
 
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GREY = (50, 50, 50)

clock = pygame.time.Clock()

def main():
    pygame.init()

    sc = pygame.display.set_mode((W, H))

    radius = 15
    color = WHITE
    last_pos = None

    font = pygame.font.SysFont('arial', 25)

    rectangle = font.render("Press W to draw rectangle", True, GREY)
    circle = font.render("Press C to draw circle", True, GREY)
    eraser = font.render("Press Space to take an eraser", True, GREY)
    red = font.render("Press R to select red", True, GREY)
    green = font.render("Press G to select green", True, GREY)
    blue = font.render("Press B to select blue", True, GREY)
    yellow = font.render("Press Y to select yellow", True, GREY)
    
    square = font.render("Press S to draw square", True, GREY) 
    right_triangle = font.render("Press T to draw right triangle", True, GREY) 
    equilateral_triangle = font.render("Press E to draw equilateral triangle", True, GREY) 
    rhombus = font.render("Press D to draw rhombus", True, GREY) 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_r:
                    color = RED
                elif event.key == pygame.K_g:
                    color = GREEN
                elif event.key == pygame.K_b:
                    color = BLUE
                elif event.key == pygame.K_y:
                    color = YELLOW
                elif event.key == pygame.K_SPACE:
                    color = BLACK

                elif event.key == pygame.K_w:
                    drawShape(sc, pygame.mouse.get_pos(), 'rectangle', color)
                elif event.key == pygame.K_c:
                    drawShape(sc, pygame.mouse.get_pos(), 'circle', color)
                elif event.key == pygame.K_s: 
                    drawShape(sc, pygame.mouse.get_pos(), 'square', color) 
                elif event.key == pygame.K_t: 
                    drawShape(sc, pygame.mouse.get_pos(), 'right_triangle', color) 
                elif event.key == pygame.K_e: 
                    drawShape(sc, pygame.mouse.get_pos(), 'equilateral_triangle', color) 
                elif event.key == pygame.K_d: 
                    drawShape(sc, pygame.mouse.get_pos(), 'rhombus', color) 

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                last_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEMOTION and event.buttons[0]:
                if last_pos is not None:
                    start_pos = last_pos
                    end_pos = pygame.mouse.get_pos()
                    drawLineBetween(sc, start_pos, end_pos, radius, color)
                    last_pos = end_pos
    
        sc.blit(rectangle, (0, 0))
        sc.blit(circle, (0, 20))
        sc.blit(eraser, (0, 40))
        sc.blit(red, (0, 60))
        sc.blit(green, (0, 80))
        sc.blit(blue, (0, 100))
        sc.blit(yellow, (0, 120))
        sc.blit(square, (0, 140)) 
        sc.blit(right_triangle, (0, 160)) 
        sc.blit(equilateral_triangle, (0, 180)) 
        sc.blit(rhombus, (0, 200)) 

        pygame.display.flip()

        clock.tick(60)

def drawLineBetween(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)
        
def drawShape(screen, mouse_pos, shape, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    if shape == 'rectangle':
        rect = pygame.Rect(x, y, 200, 100)
        pygame.draw.rect(screen, color, rect, 3)
    elif shape == 'circle':
        pygame.draw.circle(screen, color, (x, y), 100, 3)
    elif shape == 'square': 
        rect = pygame.Rect(x, y, 100, 100) 
        pygame.draw.rect(screen, color, rect, 3) 
    elif shape == 'right_triangle': 
        pygame.draw.polygon(screen, color, [(x, y), (x, y+100), (x+200, y+100)], 3) 
    elif shape == 'equilateral_triangle':
        pygame.draw.polygon(screen, color, [(x, y), (x-100, y+173), (x+100, y+173)], 3) 
    elif shape == 'rhombus': 
        pygame.draw.polygon(screen, color, [(x, y), (x+100, y+100), (x, y+200), (x-100, y+100)], 3) 

main()
