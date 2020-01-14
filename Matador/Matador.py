import random
import felter
from Spiller import *

AntalSpillere = None

print("Velkommen til Matador!")
print("Hvor mange spillere" + 
" 1 = 2 Spillere," + 
" 2 = 3 Spillere," + 
" 3 = 4 Spillere")
AntalSpillere = input()


if AntalSpillere == 2:
    print("Spiller 1 indtast navn: ")
    SpillerNavn1 = input()
    print("Spiller 2 indtast navn: ")
    SpillerNavn2 = input()
    print("Spiller 1: " + Spiller1 + "Spiller 2: " + spiller2)
else: 
    print("Sad")