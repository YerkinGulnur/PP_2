import pygame, math

display_width=800
display_height=600
game_display=pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Shape Drawer')

black=(0, 0, 0)
white=(255, 255, 255)

clock=pygame.time.Clock()

def main():
    pygame.init()
    screen=pygame.display.set_mode((640, 480))
    clock=pygame.time.Clock()
    
    radius=15
    x=0
    y=0
    mode='blue'
    points=[]
    
    while True:
        pressed=pygame.key.get_pressed()
        alt_held=pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held=pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                return
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w and ctrl_held:
                    return
                if event.key==pygame.K_F4 and alt_held:
                    return
                if event.key==pygame.K_ESCAPE:
                    return
            
                if event.key==pygame.K_r:
                    mode='red'
                elif event.key==pygame.K_g:
                    mode='green'
                elif event.key==pygame.K_b:
                    mode='blue'
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1: 
                    radius=min(200, radius + 1)
                elif event.button==3:
                    radius=max(1, radius - 1)
            
            if event.type==pygame.MOUSEMOTION:
                position=event.pos
                points=points+[position]
                points=points[-256:]
                
        screen.fill((0, 0, 0))
        
        i=0
        while i<len(points)-1:
            drawLineBetween(screen, i, points[i], points[i+1], radius, mode)
            i+=1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1=max(0, min(255, 2 * index - 256))
    c2=max(0, min(255, 2 * index))
    
    if color_mode=='blue':
        color=(c1, c1, c2)
    elif color_mode=='red':
        color=(c2, c1, c1)
    elif color_mode=='green':
        color=(c1, c2, c1)
    
    dx=start[0]-end[0]
    dy=start[1]-end[1]
    iterations=max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress=1.0*i/iterations
        aprogress=1-progress
        x=int(aprogress*start[0]+progress*end[0])
        y=int(aprogress*start[1]+progress*end[1])
        pygame.draw.circle(screen, color, (x, y), width)



def draw(self, screen, start, end):
    if self.tool_type == 'pen':
        pygame.draw.line(screen, self.color, start, end, self.size)
    elif self.tool_type == 'rectangle':
        pygame.draw.rect(screen, self.color, (start[0], start[1], end[0]-start[0], end[1]-start[1]), self.size)
    elif self.tool_type == 'circle':
        radius = int(math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2))
        pygame.draw.circle(screen, self.color, start, radius, self.size)
    elif self.tool_type == 'eraser':
        pygame.draw.line(screen, self.color, start, end, self.size)
    

def draw_square(x, y, size):

 top_left = (x, y)
 top_right = (x + size, y)
 bottom_left = (x, y + size)
 bottom_right = (x + size, y + size)

 pygame.draw.polygon(game_display, white, [top_left, top_right, bottom_right, bottom_left], 2)

 
 def draw_right_triangle(x, y, size):

  top = (x, y)
  bottom_left = (x, y+size)
  bottom_right = (x+size, y+size)
 
  pygame.draw.polygon(game_display, white, [top, bottom_left, bottom_right], 2)

def draw_equilateral_triangle(x, y, size):
  top=(x, y)
  bottom_left=(x-(size/2), y+size)
  bottom_right=(x+(size/2), y+size)
  pygame.draw.polygon(game_display, white, [top, bottom_left, bottom_right], 2)

def draw_rhombus(x, y, size):
  top=(x, y)
  right=(x + (size / 2), y + (size / 2))
  bottom=(x, y + size)
  left=(x-(size/2), y+(size/2))
  
  pygame.draw.polygon(game_display, white, [top, right, bottom, left], 2)

color_palette=pygame.display.set_mode((200, 150))
colors=[(255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
for i, color in enumerate(colors):
    pygame.draw.rect(color_palette, color, (i*25, 0, 25, 25))
pygame.display.set_caption("Select Color")

draw_square(50, 50, 100)
draw_equilateral_triangle(450, 50, 100)
draw_rhombus(650, 50, 100)



main()
