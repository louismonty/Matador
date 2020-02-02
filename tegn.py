import pygame
import draw_button
import Spiller
import time
import felter
standart_radius = 370


def tegn(screen,terning1,terning2,player_postion,x):
    screen.blit(draw_button.terning.sprite[terning1],(1000,1))
    screen.blit(draw_button.terning.sprite[terning2],(1080,1))
    for spiller in Spiller.spillere:
        draw_button.point_on_circle(32+(player_postion-1)*9%360,screen,standart_radius+spiller.radius,spiller.color)
    draw_button.text_display(30,str(Spiller.Spiller1.penge)+" "+spiller.navn,1300,100,screen)
    draw_button.text_display(30,str(spiller.ejet),1300,1000,screen)
    if x.type == "grund":
        draw_button.text_display(30, x.navn, 1500, 100,screen)
        draw_button.text_display(30, str(x.pris) + "kr", 1500, 130,screen)
        if x.købt == False:
            køb =draw_button.mousfinder(screen,1000,300,100,100,"køb")
            if køb.og == True:
                Spiller.Spiller1.penge -= x.pris
                time.sleep(0.1)
                x.købt = True
                Spiller.Spiller1.ejet += x.navn    
        else:
            draw_button.text_display(30,"allerede købt af "+Spiller.Spiller1.navn,1300,200,screen)