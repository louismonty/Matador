import random

class spiller():
    def __init__(self, navn, position, penge):
        self.navn = navn
        self.position = position
        self.penge = penge

# Variable for player1
SpillerNavn1 = "hej"
SpillerPenge1 = 30000
SpillerPosition1 = ""
# Variable for player2
SpillerNavn2 = "Farvel"
SpillerPenge2 = 30000
SpillerPosition2 = ""


Spiller1 = spiller(SpillerNavn1, 2, SpillerPenge1)
spiller2 = spiller(SpillerNavn2, 2, SpillerPenge2)

def muligheder():
    print("Velkommen til Matador!")
    print(" 1 = 2 Spillere")
    print(" 2 = 3 Spillere")
    print(" 3 = 4 Spillere")


def antalspillere():
    muligheder()
    AntalSpillere = int(input("Vælg antal spillere: "))
    while AntalSpillere > 3 or AntalSpillere <= 0:
        print("Invalid menu option.")
        AntalSpillere = int(input("Please try again: "))
    else:
        AntalSpillere = int(input())
    

def ValgteSpillere():
    AntalSpillere = antalspillere()
    if AntalSpillere == 1:
        print(" 2 spillere")
        for x in range(AntalSpillere):
            print("Hej spiller", AntalSpillere)
            AntalSpillere += 1

    elif AntalSpillere == 2:
        print("Spiller 1 indtast navn: ")
        SpillerNavn1 = input()
        print("Spiller 2 indtast navn: ")
        SpillerNavn2 = input()
        print("Spiller 1: " + Spiller1 + "Spiller 2: " + spiller2)
    else: 
        print("Sad")


ValgteSpillere()
