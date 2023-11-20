from Solver import Solver
from StonesInstance import StoneInstance, StoneSolution
import clingo as clg
import datetime as dt
import time as tm

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

        #Set board size
        control.add('base', [], f"#const n = {instance.n}.")

        #Set instance stones
        for (i, stone) in enumerate(instance.stones):
             control.add('base', [], f"stone(({stone[0]},{stone[1]}),{i+1}).")

        #Load program
        program = self.open_and_read_file()
        control.add('base', [], program)

        #Set timeout
        control.configuration.solve.timeout = tmo * 1000

        control.ground([("base", [])])

        instance.addSolution(StoneSolution([[]], 999999999, -1, -1, self.label()))

        lowest_possible_cost = 0
        if instance.n % 2 == 1 : lowest_possible_cost = 1
        lowest_possible_cost = max(lowest_possible_cost, (instance.n ** 2) - (len(instance.stones) * 2))

        #Time before solving. Needed to time the solving in case it gets interrupted early since statistics wouln't be aviable in that case
        start_time = tm.perf_counter()

        #control.solve(on_model=lambda m: self.logSolution(instance, m))
        with control.solve(yield_=True) as hnd:
            for m in hnd:

                self.logSolution(instance, m)

                end_time = tm.perf_counter()
                time = end_time - start_time

                if ( instance.solution.objective <= lowest_possible_cost or time > tmo):

                    instance.solution.solveTime = dt.timedelta(seconds=time)
                    instance.solution.flatTime = dt.timedelta(seconds=0)

                    return instance


        time = control.statistics['summary']['times']['total']

        instance.solution.solveTime = dt.timedelta(seconds=time)
        instance.solution.flatTime = dt.timedelta(seconds=0)

        return instance

    def logSolution(self, instance : StoneInstance, solution):

        solution_string = ""
        for symbol in solution.symbols(shown=True):
            solution_string += str(symbol) + " "

        try:

            #Split solution string
            values = []
            for placement_string in solution_string.split():
                values.append( placement_string.split('(')[1].strip(')').split(',') )

            #Parse placements
            placements = []
            score = 0
            for val in values:
                if (score < int(val[2])):
                    score = int(val[2])
                placements.append( {
                    'x': int(val[0]),
                    'y': int(val[1]),
                    't': int(val[2]),
                    'n': int(val[3]),
                    'ID': int(val[4])
                })

            cost = (instance.n * instance.n) - score

            if (instance.solution.objective > cost):

                print("Cost so far: " + str(cost))

                #initialize standardized solution
                std_solution = [[0 for y in range(instance.n)] for x in range(instance.n)]

                for plc in placements:
                    if not plc['t'] == 0:
                        if instance.stones[plc['ID'] - 1][0] == plc['n']:
                            sign = +1
                        else:
                            sign = -1

                        std_solution[plc['x'] - 1][plc['y'] - 1] = sign * plc['ID']

                instance.solution.placements = std_solution
                instance.solution.objective = cost

        except:

            print("Some error occurred while logging solution. Printing the solution string:")
            print(solution_string)



            
