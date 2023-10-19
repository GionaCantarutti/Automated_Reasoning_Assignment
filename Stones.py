from StonesInstance import StoneInstance
from MiniZincA import MiniZincA
from MiniZincB import MiniZincB

TIMEOUT = 5 * 60

EASY_SIZE = 10
EASY_TILECOUNT = 60

MEDIUM_SIZE = 11
MEDIUM_TILECOUNT = 100

HARD_SIZE = 15
HARD_TILECOUNT = 120

#MiniZincB performa molto meglio quando gli vengono date abbastanza tiles. Oltre ad un certo punto aumentare le tiles smette di avere un costo sulla performance
#MiniZincB andrà in timeout per n=11 con 70 tiles (poco più del minimo necessario per coprire la grid) ma riesce a risolvere l'istanza n11 con 120 tiles in soli 25 secondi
#MiniZincA probabilmente non funziona alla stessa maniera, da testare

newInstance = StoneInstance.generateRandom(MEDIUM_SIZE, MEDIUM_TILECOUNT)
print((MiniZincB.solveInstance(newInstance, TIMEOUT)).solutionString())