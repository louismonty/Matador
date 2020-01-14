import pygame
class player:
    player_positon_x = 1
    player_positon_y = 1
    money = 30000

class terning:
    sprite = [pygame.image.load('dice1.png'),pygame.image.load('dice2.png'), pygame.image.load('dice3.png'),pygame.image.load('dice4.png'),pygame.image.load('dice5.png'),pygame.image.load('dice6.png')]

class grunde():
    def __init__(self,feltnumber,name,color,prices):
        self.feltnumber = feltnumber 
        self.name = name
        self.color = color
        self.prices = prices
        self.houses = 0
        self.ejer = False
    
    def excute(x):
        print("works")

    def __str__(self):
        return(self.name,"is")

    felter = ["Rødeovrevej","Prøv løkken","Hvidovrevej","Betal indkomstskat","SFL skib","Roskildevej","Prøve lykken","Balby langgade","Allegade","I fængsel","Frederiksberg alle","Tuborg","Bülowsvej","Gl. Kongevej","Kalundborg/århus",]

class færge():
    def __init__(self,feltnummer,name,price):
        self.feltnumber = feltnummer
        self.name = name
        self.price = price
        self.ejer = False

class knap():
    def __init__(tekst,size,box_x,box_y,box_size_x,box_size_y):
        pygame.font.init()
        box_font = pygame.font.SysFont('Comic Sans MS', size)
 


two = grunde(2,"Rødovrevej","blå",1200)
four = grunde(4,"hvidovrevej","blå",1200)
six = færge(6,"SFL",4000)

class start:
    typ = True
    def excute():
        player.money +=2000
        print(player.money)

def tax():
    if(player.money/10<=4000):
        player.money-4000
        print("du betalete",player.money/10,"i skal")
    else:
        print("du betaler 4000 i skat",player.money/10)


def prøv_lykken():
    print("prøv lykken")

def indirect(i):
    switcher={
        1:start,
        2:two,
        3:prøv_lykken,
        4:four, 
        5:tax,

    }
    return(switcher.get(i))