import time
import pygame 
from math import cos, sin, pi

pygame.init() 
  

#---- RBG color---------
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
#-----------------------
  

X = 1920
Y = 1080
  

display_surface = pygame.display.set_mode((X, Y )) 
pygame.display.set_caption("Matador") 
image = pygame.image.load("matador_plade1.jpg") 

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_display(text_size, text, text_x, text_y):
    largeText = pygame.font.SysFont("Times new Roman",text_size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (text_x,text_y)
    screen.blit(TextSurf, TextRect)

def point_on_circle(angle):
   
    radius = 370
    x_origin = 480
    y_origin = 480
    x = x_origin + radius * cos(angle * pi / 180)
    y = y_origin + radius * sin(angle * pi / 180)

    pygame.draw.circle(display_surface, blue,(int(x),int(y)), 10)
    print(x,y)
    return x,y

i=0
   
# infinite loop 
while True : 
    display_surface.fill(white) 
    display_surface.blit(image, (0, 0)) 
    
    i = 1
    point_on_circle(32+(i-1)*9%360)
    #pygame.draw.circle(display_surface, blue,(480,480), 370)
    time.sleep(1)
    mouse = pygame.mouse.get_pos()
    print(mouse)
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
  
            # quit the program. 
            quit() 
  
        # Draws the surface object to the screen.   
        pygame.display.update()  
