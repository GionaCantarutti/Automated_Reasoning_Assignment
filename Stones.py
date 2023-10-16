from StonesInstance import StoneInstance
from MiniZincA import MiniZincA
from MiniZincB import MiniZincB

newInstance = StoneInstance.generateRandom(5, 10)
print((MiniZincB.solveInstance(newInstance, 10)).solutionString())