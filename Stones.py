from StonesInstance import StoneInstance
from MiniZincA import MiniZincA
from MiniZincB import MiniZincB
from TestBatch import TestBatch
from SolutionsLogger import SolutionsLogger
from StatisticsLogger import StatisticsLogger
import os
from datetime import datetime
from Batches import *
from ModelSets import *

TIMEOUT = 5 * 60

SOLVERS = FINAL_TESTING_C

BATCHES = EXAUSTIVE

def print_report():
    progress = reps_done/total_reps
    print("Spent " + "{:.2f}".format(elapsed/60.0) + " minutes out of " + "{:.2f}".format(max_time/60.0) + " aviable, " + "{:.2f}".format((max_time - elapsed)/60.0) + " left")
    print("Current progress is " + "{:.2f}".format(progress*100) + "% by repetitions and " + "{:.2f}".format(elapsed/max_time * 100) + "% by maximum allowed time")

local_path = os.getcwd()
new_dir_path = os.path.join(local_path, "benchmarks", datetime.now().strftime("%d-%m-%Y_%H.%M.%S"))
os.mkdir(new_dir_path)

stats = [[StatisticsLogger(StatisticsLogger.createName(solver, batch), batch.size, batch.tilecount, solver.label(), TIMEOUT) for solver in SOLVERS] for batch in BATCHES]

StatisticsLogger.init_file(new_dir_path)

elapsed = 0
max_time = TOTAL_TIME_BUDGET_PER_SOLVER * len(SOLVERS)
total_reps = 0
for batch in BATCHES:
    total_reps += batch.repetitions
total_reps *= len(SOLVERS)
reps_done = 0

for bi, batch in enumerate(BATCHES):    
    log_file = SolutionsLogger.open_logfile(new_dir_path)
    for i in range(batch.repetitions):
        newInstance = StoneInstance.generateRandom(batch.size, batch.tilecount)
        for si, solver in enumerate(SOLVERS):

            if solver.tBudget_left() <= 0:
                print_report()
                print(solver.label() + " solver ran out of time, moving on\n")
                stats[bi][si].log_timeout()
                reps_done += 1
                continue

            print_report()
            print(batch.label + " batch with " + solver.label() + " solver, repetition " + str(i + 1) + "/" + str(batch.repetitions) + " ...\n")
            
            solved = solver.solveInstance(newInstance, TIMEOUT)
            time_spent = max(1, solved.solution.solveTime.seconds + solved.solution.flatTime.seconds)
            solver.spend_time(time_spent)
            elapsed += time_spent

            SolutionsLogger.log_new(solved, log_file)
            stats[bi][si].add_data(solved)
            reps_done += 1
        

    stats_file = StatisticsLogger.open_file(new_dir_path)
    for j in range(len(SOLVERS)):
        stats[bi][j].log_line(stats_file)
    StatisticsLogger.close_file(stats_file)
    SolutionsLogger.close_logfile(log_file)
        

print("DONE!")

#MiniZincB performa molto meglio quando gli vengono date abbastanza tiles. Oltre ad un certo punto aumentare le tiles smette di avere un costo sulla performance
#MiniZincB andrà in timeout per n=11 con 70 tiles (poco più del minimo necessario per coprire la grid) ma riesce a risolvere l'istanza n11 con 120 tiles in soli 25 secondi
#MiniZincA probabilmente non funziona alla stessa maniera, da testare

#newInstance = StoneInstance.generateRandom(EASY_SIZE, EASY_TILECOUNT)
#solverB = MiniZincB("Stones3.mzn")
#print((solverB.solveInstance(newInstance, TIMEOUT)).solutionString())