from Solver import Solver
from StonesInstance import StoneInstance, StoneSolution
import minizinc as mzn
import datetime as dt

class MiniZincA(Solver):

    def __init__(self, path, label, timeBudget):
        self.file = path
        self.name = label
        self.time_budget = timeBudget

    def solveInstance(self, instance: StoneInstance, tmo):
        model = mzn.Model()
        model.add_file(self.file)

        gecode = mzn.Solver.lookup("gecode")

        inst = mzn.Instance(gecode, model)

        inst["n"] = instance.n
        inst["t"] = len(instance.stones)
        inst["Stones"] = instance.stones

        rawSolution = inst.solve(intermediate_solutions=True, timeout=dt.timedelta(seconds=tmo))

        #Log all partial solutions (legacy, to remove)
        for i in range(rawSolution.__len__()):
            placements = rawSolution.__getitem__((i, "Placements"))
            coordinates = rawSolution.__getitem__((i, "Coordinates"))
            sides = rawSolution.__getitem__((i, "Sides"))
            obj = rawSolution.__getitem__(i).objective
#            print(placements)
#            print("Empty spaces left: " + str(rawSolution.__getitem__(i).objective) + " of a minimum of " + str(max(instance.n**2 - len(instance.stones)*2,0)))
#            print("___________________________")

        solution = [[0 for y in range(instance.n)] for x in range(instance.n)]

        
        if rawSolution.__len__() <= 0:
            instance.addSolution(StoneSolution(solution, None, dt.timedelta(seconds=min(tmo, self.time_budget)), dt.timedelta(seconds=0), self.name))
            return instance
        
        flatTime = rawSolution.statistics["flatTime"]
        solveTime = rawSolution.statistics["solveTime"]

        for i in range(len(placements)):
            if placements[i] != 0:
                # That somewhat convoluted operation on sides[i] simply maps 1->2 and 2->-1
                solution[coordinates[0][i] - 1][coordinates[1][i] - 1] = ((2 - sides[i]) * 2 - 1) * placements[i]

        instance.addSolution(StoneSolution(solution, obj, solveTime, flatTime, self.name))
        return instance

