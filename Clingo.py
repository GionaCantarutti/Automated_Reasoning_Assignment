from Solver import Solver
from StonesInstance import StoneInstance, StoneSolution
import clingo as clg
import datetime as dt

class Clingo(Solver):

    def __init__(self, path, label, timeBudget):
        self.file = path
        self.name = label
        self.time_budget = timeBudget

    def open_and_read_file(self):
         file = open(self.file, "r")
         data = file.read()
         file.close()
         return data

    def solveInstance(self, instance: StoneInstance, tmo):
       
        control = clg.Control(['--stats'])

        program = self.open_and_read_file()

        control.add('base', [], program)

        #Set timeout
        control.configuration.solve.timeout = tmo * 1000

        control.ground([("base", [])])

        instance.addSolution(StoneSolution([[]], 999999999, -1, -1, self.label()))

        control.solve(on_model=lambda m: self.logSolution(instance, m))

        time = control.statistics['summary']['times']['total']

        instance.solution.solveTime = dt.timedelta(seconds=time)
        instance.solution.flatTime = dt.timedelta(seconds=0)

        return instance

    def logSolution(self, instance, solution):

        objective_value = 0
        
        solution_string = ""
        for symbol in solution.symbols(shown=True):
            solution_string += str(symbol) + " "
            if symbol.name == "objective":
                objective_value = int(symbol.arguments[0])
                break

        #Check if solution is better than currently logged one
        if instance.solution.objective > objective_value:

            instance.solution.objective = objective_value

            #Split solution string
            values = []
            for placement_string in solution_string.split():
                values.append( placement_string.split('(')[1].strip(')').split(',') )

            #Parse placements
            placements = []
            for val in values:
                placements.append( {
                    'x': int(val[0]),
                    'y': int(val[1]),
                    't': int(val[2]),
                    'n': int(val[3]),
                    'ID': int(val[4])
                })

            #initialize standardized solution
            std_solution = [[0 for y in range(instance.n)] for x in range(instance.n)]

            for plc in placements:
                if instance.stones[plc['ID'] - 1][0] == plc['n']:
                    sign = +1
                else:
                    sign = -1

                std_solution[plc['x'] - 1][plc['y'] - 1] = sign * plc['ID']

            instance.solution.placements = std_solution

            
