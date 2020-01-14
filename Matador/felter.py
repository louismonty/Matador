class grunde():
    class grund():
        def __init__(self, navn, pris):
            self.type = "grund"
            self.navn = navn
            self.pris = pris

    class bryggeri():
        def __init__(self, navn, pris):
            self.type = "grund"
            self.navn = navn
            self.pris = pris

    class færge():
        def __init__(self, navn, pris):
            self.type = "grund"
            self.navn = navn
            self.pris = pris


class hændelse():
    class prøv_lykken():
        def __init__(self, nothing):
            self.type = "prøv_lykken"
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
rødovrevej = grunde.grund(("rødovrevej"), 1200)
prøv_lykken = hændelse.prøv_lykken(("prøv lykken"))
hvidovrevej = grunde.grund(("Hvidovrevej"), 1200)
betal_skat = hændelse.betal_skat(("Betal skat"), 4000)
færge = grunde.færge(("færge"), 4000)
roskildevej = grunde.grund(("Roskildevej"), 2000)
valby_langgade = grunde.grund(("Valby Langgade"), 2000)
Allegade = grunde.grund(("Allégade"), 2400)
gå_i_fængsel = hændelse.gå_i_fængsel(("gå i fængsel"))
Frederiksberg_alle = grunde.grund(("Frederiksberg Alle"), 2800)
tuborg = grunde.bryggeri(("Tuborg"), 3000)
bulowsvej = grunde.grund(("Bülowsvej"), 2800)
gammel_kongevej = grunde.grund(("Gl. Kongevej"), 3200)
bernstorffsvej = grunde.grund(("Bernstorffsvej"), 3600)
hellerupvej = grunde.grund(("Hellerupvej"), 3600)
strandvej = grunde.grund(("Strandvej"), 4000)
parkering = hændelse.parkering(("Parkering")) # Mangler hændelse
trianglen = grunde.grund(("Trianglen"), 4400)
østerbrogade = grunde.grund(("Østerbrogade"), 4400)
grønningen = grunde.grund(("Grønnningen"), 4800)
bredgade = grunde.grund(("Bredgade"), 5200)
nytorv = grunde.grund(("Kgs. Nytorv"), 5200) 
cocacola = grunde.bryggeri(("Coca Cola"), 3000)
østergade = grunde.grund(("Østergade"), 5600)
amagertorv = grunde.grund(("Amagertorv"), 6000)
vimmelskaftet = grunde.grund(("Vimmelskaftet"), 6000)
nygade = grunde.grund(("Nygade"), 6400)
Frederiksberggade = grunde.grund(("Frederiksberg gade"), 7000)
rådhuspladsen = grunde.grund(("Rådhuspladsen"), 8000)






felter = [start, rødovrevej, prøv_lykken, hvidovrevej, betal_skat, færge, roskildevej, prøv_lykken, valby_langgade, Allegade, gå_i_fængsel, Frederiksberg_alle, tuborg, bulowsvej, gammel_kongevej,
færge, bernstorffsvej, prøv_lykken, hellerupvej, strandvej, parkering, trianglen, prøv_lykken, østerbrogade, grønningen, færge, bredgade, nytorv, cocacola, østergade, gå_i_fængsel, amagertorv
, vimmelskaftet, prøv_lykken, nygade, færge, prøv_lykken, Frederiksberggade, betal_skat, rådhuspladsen]

