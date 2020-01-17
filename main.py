import pygame,time,random
import draw_button
import felter
import Spiller

pygame.init()
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
map = pygame.image.load('map.jpg')

def Terning_slag():
    return int(random.uniform(0,6)),int((random.uniform(0,6)))


def game_loop():

    player_postion = 1
    terning1 , terning2 = 0,0
    exit = False

    while exit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        x=felter.felter[player_postion-1]
        
        print(pygame.mouse.get_pos())

        screen.fill(draw_button.white) 
        screen.blit(map,(1,1))
        test =draw_button.mousfinder(screen,10,10,100,100,"test")
        if(test.og == True):
            terning1,terning2=Terning_slag()
            player_postion = (player_postion+terning1+1+terning2+1)%40
            time.sleep(0.1)
        #print(player_postion)
        screen.blit(draw_button.terning.sprite[terning1],(1000,1))
        screen.blit(draw_button.terning.sprite[terning2],(1080,1))
        draw_button.point_on_circle(32+(player_postion-1)*9%360,screen)
        draw_button.text_display(60,str(player_postion),100,100,screen)
        draw_button.text_display(30,str(Spiller.Spiller1.penge)+ "spiller 1",1300,100,screen)
        if x.type == "grund":
            #print(x.navn)
            køb = draw_button.mousfinder(screen,1400,300,100,100,"køb")
            draw_button.text_display(30, x.navn, 1500, 100,screen)
            draw_button.text_display(30, str(x.pris) + "kr", 1500, 130,screen)
            if køb.og == True:
                Spiller.Spiller1.penge -= x.pris
                time.sleep(0.1)
        pygame.display.flip()

game_loop()
