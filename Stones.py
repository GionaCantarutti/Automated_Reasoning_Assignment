from StonesInstance import StoneInstance
from MiniZincA import MiniZincA

newInstance = StoneInstance.generateRandom(5, 10)
print((MiniZincA.solveInstance(newInstance, 10)).solutionString())