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

newInstance = StoneInstance.generateRandom(MEDIUM_SIZE, MEDIUM_TILECOUNT)
print((MiniZincB.solveInstance(newInstance, TIMEOUT)).solutionString())