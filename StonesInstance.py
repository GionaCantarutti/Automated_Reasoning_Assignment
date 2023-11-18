import random as r

class StoneSolution:

    def __init__(self, placements, objective, solveTime, flatTime, solverLabel):
        # Bidimensional array of stone indexes. Negative if it's supposed to point at the "back side" of a stone
        # 0 means no placement
        # the index is that of an array that starts at 1
        self.placements = placements
        self.solveTime = solveTime
        self.flatTime = flatTime
        self.solverUsed = solverLabel
        self.objective = objective

class StoneInstance:
    
    def __init__(self, n: int, stones):
        self.n = n
        self.stones = stones
        self.solution : StoneSolution = None

    def addSolution(self, solution: StoneSolution):
        self.solution = solution

    def generateRandom(n, tCount):
        st = []
        for i in range(tCount):
            st.append([r.randint(0,6),r.randint(0,6)])
        
        return StoneInstance(n, st)
    
    def simple():
        return StoneInstance(3, [[1,2],[2,3],[3,4]])
    
    def solutionString(self):
        plc = self.solution.placements
        # Make a grid of characters with added spaces between tile values
        stringGrid = [[" " for x in range(self.n*2 - 1)] for y in range(self.n*2 - 1)]

        #print("Stones:\n" + str(self.stones) + "\n\nSolution:")

        # First pass to populate the tile values
        for x, line in enumerate(plc):
            for y, placement in enumerate(line):
                if placement == 0:
                    stringGrid[x*2][y*2] = "#"
                    continue
                if placement > 0:
                    face = 0
                elif placement < 0:
                    face = 1
                stringGrid[x*2][y*2] = str(self.stones[abs(placement) - 1][face])

        # Second pass to add connections
        for x, line in enumerate(plc):
            for y, placement in enumerate(line):
                if y < len(line)-1:
                    if (abs(placement) == abs(line[y+1])) & (placement != 0):
                        stringGrid[x*2][y*2+1] = "-"
                if x < len(plc)-1:
                    if (abs(placement) == abs(plc[x+1][y])) & (placement != 0):
                        stringGrid[x*2+1][y*2] = "|"

        # Turn the grid into a single string and return it
        finalString = ""
        for line in stringGrid:
            for element in line:
                finalString += element
            finalString += "\n"
        return finalString


    

