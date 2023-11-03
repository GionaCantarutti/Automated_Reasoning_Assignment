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
        
        for symbol in solution.symbols(shown=True):
            if symbol.name == "objective":
                objective_value = int(symbol.arguments[0])
                break

        #Check if solution is better than currently logged one
        if instance.solution.objective > objective_value:

            print(solution)

            instance.solution.objective = objective_value
