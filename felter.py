class grunde():
    def __init__(self, navn, pris,felt):
        self.type = "grund"
        self.navn = navn
        self.pris = pris
        self.købt = False
        self.felt = felt
class grund(grunde):
    hus = 0
    multiplikator = 0.2


class bryggeri(grunde):
    antal_ejet = 0
    multiplikator = 0.5


class færge(grunde):
    antal_ejet = 0
    multiplikator = 0.4



class hændelse():
    class prøv_lykken():
        def __init__(self, nothing):
            self.type = "fængsel"
            self.nothing = nothing

    
    class gå_i_fængsel():
        def __init__(self, nothing):
            self.type = "fængsel"
            self.nothing = nothing

    class parkering():
        def __init__(self, nothing):
            self.type = "parkering"
            self.nothing = nothing

    class betal_skat():
        def __init__(self, navn, pris):
            self.type = "skat"
            self.navn = navn
            self.pris = pris

class stadie():
    class fængsel():
        def __init__(self, navn):
            self.type = "fængsel"
            self.navn = navn

    class start():
        def __init__(self, navn, pris):
            self.type = "start"
            self.navn = navn
            self.pris = pris
    
start = stadie.start(("start"), 4000)
rødovrevej = grund(("rødovrevej"), 1200,2)
prøv_lykken = hændelse.prøv_lykken(("prøv lykken"))
hvidovrevej = grund(("Hvidovrevej"), 1200,4)
betal_skat = hændelse.betal_skat(("Betal skat"), 4000)
færge = færge(("færge"), 4000,6)
roskildevej = grund(("Roskildevej"), 2000,7)
valby_langgade = grund(("Valby Langgade"), 2000,9)
Allegade = grund(("Allégade"), 2400,10)
gå_i_fængsel = hændelse.gå_i_fængsel(("gå i fængsel"))
Frederiksberg_alle = grund(("Frederiksberg Alle"), 2800,12)
tuborg = bryggeri(("Tuborg"), 3000,13)
bulowsvej = grund(("Bülowsvej"), 2800,14)
gammel_kongevej = grund(("Gl. Kongevej"), 3200,15)
bernstorffsvej = grund(("Bernstorffsvej"), 3600,17)
hellerupvej = grund(("Hellerupvej"), 3600,19)
strandvej = grund(("Strandvej"), 4000,20)
parkering = hændelse.parkering(("Parkering")) # Mangler hændelse
trianglen = grund(("Trianglen"), 4400,12)
østerbrogade = grund(("Østerbrogade"), 4400,24)
grønningen = grund(("Grønnningen"), 4800,25)
bredgade = grund(("Bredgade"), 5200,27)
nytorv = grund(("Kgs. Nytorv"), 5200,28) 
cocacola = bryggeri(("Coca Cola"), 3000,29)
østergade = grund(("Østergade"), 5600,30)
amagertorv = grund(("Amagertorv"), 6000,32)
vimmelskaftet = grund(("Vimmelskaftet"), 6000,33)
nygade = grund(("Nygade"), 6400,35)
Frederiksberggade = grund(("Frederiksberg gade"), 7000,38)
rådhuspladsen = grund(("Rådhuspladsen"), 8000,40)






felter = [start, rødovrevej, prøv_lykken, hvidovrevej, betal_skat, færge, roskildevej, prøv_lykken, valby_langgade, Allegade, gå_i_fængsel, Frederiksberg_alle, tuborg, bulowsvej, gammel_kongevej,
færge, bernstorffsvej, prøv_lykken, hellerupvej, strandvej, parkering, trianglen, prøv_lykken, østerbrogade, grønningen, færge, bredgade, nytorv, cocacola, østergade, gå_i_fængsel, amagertorv
, vimmelskaftet, prøv_lykken, nygade, færge, prøv_lykken, Frederiksberggade, betal_skat, rådhuspladsen]

