class spiller():
    def __init__(self, navn, position, penge,color,radius):
        self.navn = navn
        self.position = position
        self.penge = penge
        self.ejet = []
        self.color = color
        self.radius = radius

# Variable for player1
SpillerNavn1 = "spiller1"
SpillerPenge1 = 30000
SpillerPosition1 = ""
# Variable for player2
SpillerNavn2 = "spiller2"
SpillerPenge2 = 30000
SpillerPosition2 = ""


Spiller1 = spiller(SpillerNavn1, 2, SpillerPenge1,(255,0,0),0)
spiller2 = spiller(SpillerNavn2, 2, SpillerPenge2,(255,255,0),20)

spillere= [Spiller1,spiller2]