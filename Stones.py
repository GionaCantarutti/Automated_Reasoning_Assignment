from StonesInstance import StoneInstance
from MiniZincA import MiniZincA
from MiniZincB import MiniZincB

TIMEOUT = 5 * 60

EASY_SIZE = 6
EASY_TILECOUNT = 20

MEDIUM_SIZE = 10
MEDIUM_TILECOUNT = 60

HARD_SIZE = 15
HARD_TILECOUNT = 120

newInstance = StoneInstance.generateRandom(MEDIUM_SIZE, MEDIUM_TILECOUNT)
print((MiniZincB.solveInstance(newInstance, TIMEOUT)).solutionString())