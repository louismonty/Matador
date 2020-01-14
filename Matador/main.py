import pygame
import random
import time
import classess
import idk
import elster
import felter
import Spiller
def Terning_slag():
    # (spiller_postion+int(random.uniform(1,6))+int(random.uniform(1,6)))%40
    return int(random.uniform(0,6)),int((random.uniform(0,6)))
player_postion = 1
terning1 , terning2 = 0,0
pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
map = pygame.image.load('map.jpg')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    x=felter.felter[player_postion-1]
    
    print(pygame.mouse.get_pos())

    screen.fill(elster.white) 
    screen.blit(map,(1,1))
    test =idk.mousfinder(screen,10,10,100,100,"test")
    if(test.og == True):
        terning1,terning2=Terning_slag()
        player_postion = (player_postion+terning1+1+terning2+1)%40
        time.sleep(0.1)
    #print(player_postion)
    screen.blit(classess.terning.sprite[terning1],(1000,1))
    screen.blit(classess.terning.sprite[terning2],(1080,1))
    elster.point_on_circle(32+(player_postion-1)*9%360,screen)
    elster.text_display(60,str(player_postion),100,100,screen)
    elster.text_display(30,str(Spiller.Spiller1.penge)+ "spiller 1",1300,100,screen)
    if x.type == "grund":
        #print(x.navn)
        køb = idk.mousfinder(screen,1400,300,100,100,"køb")
        elster.text_display(30, x.navn, 1500, 100,screen)
        elster.text_display(30, str(x.pris) + "kr", 1500, 130,screen)
        if køb.og == True:
            Spiller.Spiller1.penge -= x.pris
            time.sleep(0.1)
    pygame.display.flip()

