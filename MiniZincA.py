from Solver import Solver
from StonesInstance import StoneInstance, StoneSolution
import minizinc as mzn
import datetime

class MiniZincA(Solver):

    def solveInstance(instance: StoneInstance, tmo):
        model = mzn.Model()
        model.add_file("Stones2.mzn")

        gecode = mzn.Solver.lookup("gecode")

        inst = mzn.Instance(gecode, model)

        inst["n"] = instance.n
        inst["t"] = len(instance.stones)
        inst["Stones"] = instance.stones

        rawSolution = inst.solve(intermediate_solutions=True, timeout=datetime.timedelta(seconds=tmo))

        for i in range(rawSolution.__len__()):
            placements = rawSolution.__getitem__((i, "Placements"))
            coordinates = rawSolution.__getitem__((i, "Coordinates"))
            sides = rawSolution.__getitem__((i, "Sides"))
#            print(placements)
#            print("Empty spaces left: " + str(rawSolution.__getitem__(i).objective) + " of a minimum of " + str(max(instance.n**2 - len(instance.stones)*2,0)))
#            print("___________________________")

        solution = [[0 for y in range(instance.n)] for x in range(instance.n)]

        for i in range(len(placements)):
            if placements[i] != 0:
                # That somewhat convoluted operation on sides[i] simply maps 1->2 and 2->-1
                solution[coordinates[0][i] - 1][coordinates[1][i] - 1] = ((2 - sides[i]) * 2 - 1) * placements[i]

        instance.addSolution(StoneSolution(solution))
        return instance

