import pygame,time,random
import draw_button
import felter
import Spiller
import tegn

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
map = pygame.image.load(
    'map.jpg')

def Terning_slag():
    return int(random.uniform(0,6)),int((random.uniform(0,6)))



def game_loop(antalspillere ):

    player_postion = 1
    terning1 , terning2 = 0,0
    exit = False

    while exit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        x=felter.felter[player_postion-1]
        screen.fill(draw_button.white) 
        screen.blit(map,(1,1))
        test =draw_button.mousfinder(screen,10,10,100,100,"slå")
        if(test.og == True):
            terning1,terning2=Terning_slag()
            player_postion = (player_postion+terning1+1+terning2+1)%40
            time.sleep(0.1)
        tegn.tegn(screen,terning1,terning2,player_postion,x)
        pygame.display.flip()

def Valg_af_spiller():
    Antalspillere = input("hvor mange spiller vil du være ")
    game_loop(Antalspillere)

Valg_af_spiller()

#game_loop()

