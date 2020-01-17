import time
import pygame 
from math import cos, sin, pi

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_display(text_size, text, text_x, text_y,screen):
    largeText = pygame.font.SysFont("Times new Roman",text_size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (text_x,text_y)
    screen.blit(TextSurf, TextRect)

def point_on_circle(angle,screen):
    radius = 370
    x_origin = 480
    y_origin = 480
    x = x_origin + radius * cos(angle * pi / 180)
    y = y_origin + radius * sin(angle * pi / 180)
    pygame.draw.circle(screen, blue,(int(x),int(y)), 10)
    return x,y
