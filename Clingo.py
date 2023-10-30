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
       
        control = clg.Control()

        program = self.open_and_read_file()

        with control.builder() as bld:
                clg.parse_program(program, lambda stm: bld.add(stm))

        control.ground([("base", [])])

        #To properly read answer and insert in the instance
        control.solve(on_model=lambda m: print("Answer: {}".format(m)))
