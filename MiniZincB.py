from Solver import Solver
from StonesInstance import StoneInstance, StoneSolution
import minizinc as mzn
import datetime as dt
import numpy as np

class MiniZincB(Solver):

    def __init__(self, path, label, timeBudget):
        self.file = path
        self.name = label
        self.time_budget = timeBudget
        
    def solveInstance(self, instance: StoneInstance, tmo):
        model = mzn.Model()
        model.add_file(self.file)

        gecode = mzn.Solver.lookup("gecode")

        inst = mzn.Instance(gecode, model)

        # Build stone matrix as input
        stoneMatrix = [[0 for x in range(7)] for y in range(7)]
        for s in instance.stones:
            stoneMatrix[s[0]][s[1]] += 1
            stoneMatrix[s[1]][s[0]] += 1

        inst["n"] = instance.n
        inst["Stones"] = stoneMatrix

        #print(np.array(stoneMatrix))

        rawSolution = inst.solve(intermediate_solutions=True, timeout=dt.timedelta(seconds=tmo))

        for i in range(rawSolution.__len__()):
            placements = np.transpose(rawSolution.__getitem__((i, "Placements")))
            coordinates = rawSolution.__getitem__((i, "Coordinates"))
            obj = rawSolution.__getitem__(i).objective
            #print("Empty spaces left: " + str(rawSolution.__getitem__(i).objective) + " of a minimum of " + str(max(instance.n**2 - len(instance.stones)*2,0)))
            #print("Placemnts:\n" + str(np.transpose(placements)))
            #print("Coodrds:\n" + str(np.matrix(coordinates)))
            #print("Stone matrix:\n" + str(np.matrix(stoneMatrix)))
            #print("___________________________")

        solution = [[0 for y in range(instance.n)] for x in range(instance.n)]


        if rawSolution.__len__() <= 0:
            instance.addSolution(StoneSolution(solution, None, dt.timedelta(tmo), dt.timedelta(seconds=0), self.name))
            return instance
        
        try:
            flatTime = rawSolution.statistics["flatTime"]
        except:
            flatTime = dt.timedelta(seconds=0)
        try:
            solveTime = rawSolution.statistics["solveTime"]
        except:
            solveTime = dt.timedelta(seconds=0)

        assigned = [False for x in range(len(placements))]

        #Find where each stone has been placed, if anywhere
        for i, stone in enumerate(instance.stones):
            for pi, placement in enumerate(placements):
                if (not assigned[pi]) and (stone[0] == (placement[0] - 1)) and (stone[1] == (placement[1] - 1)):
                    #Stone matched to placement, now if placement index is even the next placement has the back side, the previous placement has it otherwise
                    if (pi % 2 == 0):
                        solution[coordinates[0][pi] - 1][coordinates[1][pi] - 1] = (i + 1)
                        solution[coordinates[0][pi + 1] - 1][coordinates[1][pi + 1] - 1] = -(i + 1)
                        assigned[pi+1] = True
                    else:
                        solution[coordinates[0][pi] - 1][coordinates[1][pi] - 1] = (i + 1)
                        solution[coordinates[0][pi - 1] - 1][coordinates[1][pi - 1] - 1] = -(i + 1)
                        assigned[pi-1] = True
                    assigned[pi] = True
                    break

        instance.addSolution(StoneSolution(solution, obj, solveTime, flatTime, self.name))
        return instance