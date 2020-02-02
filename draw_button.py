import pygame
import time
from math import cos, sin, pi
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

def box(screen):
    pygame.draw.rect(screen, (0,250,0),pygame.Rect(10, 10, 100, 100))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

class mousfinder():
    

    def __init__(self,screen,x,y,size_x,size_y,text):
        m_x,m_y = pygame.mouse.get_pos()
        pygame.draw.rect(screen, (0,250,0),pygame.Rect(x, y, size_x,size_y))
        largeText = pygame.font.SysFont("Times new Roman",int(size_x/2))
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = (x+(size_x/2),y+(size_x/2))
        screen.blit(TextSurf, TextRect)
        if(m_x>x and m_x<(x+size_x)and m_y>y and m_y<(y+size_y)):
            if pygame.mouse.get_pressed()[0]:
                self.og=True
            else:
                self.og = False
        else:
            self.og = False


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_display(text_size, text, text_x, text_y,screen):
    largeText = pygame.font.SysFont("Times new Roman",text_size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (text_x,text_y)
    screen.blit(TextSurf, TextRect)

def point_on_circle(angle,screen,radius,color):
    x_origin = 480
    y_origin = 480
    x = x_origin + radius * cos(angle * pi / 180)
    y = y_origin + radius * sin(angle * pi / 180)
    pygame.draw.circle(screen, color,(int(x),int(y)), 10)
    return x,y


class terning:
    sprite = [pygame.image.load('dice1.png'),pygame.image.load('dice2.png'), pygame.image.load('dice3.png'),pygame.image.load('dice4.png'),pygame.image.load('dice5.png'),pygame.image.load('dice6.png')]


    