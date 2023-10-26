from StonesInstance import StoneInstance
from MiniZincA import MiniZincA
from MiniZincB import MiniZincB
from TestBatch import TestBatch
from SolutionsLogger import SolutionsLogger
from StatisticsLogger import StatisticsLogger
import os
from datetime import datetime

TIMEOUT = 5 * 60
TOTAL_TIME_BUDGET_PER_SOLVER = 4 * TIMEOUT

#Seemingly unfixable, cannot use non-fixed variables in relax_and_reconstruct :(
NONPLACEMENT_FIX = [
    MiniZincB("Models/Minizinc/Improved coordinates/prevent zigzag.mzn", "no restart", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 50 nonplacements fix.mzn", "luby 50 fixed", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 50.mzn", "luby 50 not fixed", TOTAL_TIME_BUDGET_PER_SOLVER),
]

KEEP_CHANCE_B = [
    MiniZincB("Models/Minizinc/Improved coordinates/prevent zigzag.mzn", "no restart", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 15.mzn", "luby 15", TOTAL_TIME_BUDGET_PER_SOLVER),s
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 30.mzn", "luby 30", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 50.mzn", "luby 50", TOTAL_TIME_BUDGET_PER_SOLVER),
]

KEEP_CHANCE = [
    MiniZincB("Models/Minizinc/Improved coordinates/prevent zigzag.mzn", "no restart", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/constant 30.mzn", "constant 30", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/constant 90.mzn", "constant 90", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 30.mzn", "luby 30", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 90.mzn", "luby 90", TOTAL_TIME_BUDGET_PER_SOLVER),
]

LNS = [
    MiniZincB("Models/Minizinc/Improved coordinates/prevent zigzag.mzn", "no restart", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/constant restart.mzn", "constant restart", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/linear restart.mzn", "linear restart", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/geometric restart.mzn", "geometric restart", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/luby restart.mzn", "luby restart", TOTAL_TIME_BUDGET_PER_SOLVER),
]

BATCH_TUNING = [MiniZincB("Models/Minizinc/Improved coordinates/prevent zigzag.mzn", "best model so far", TOTAL_TIME_BUDGET_PER_SOLVER),]

ZIGZAG_PREVENTION = [
    MiniZincB("Models/Minizinc/Improved coordinates/prevent zigzag.mzn", "with prevention", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/input_order indomain_min.mzn", "without prevention", TOTAL_TIME_BUDGET_PER_SOLVER),
]

#Note: not using indomain_min for coordinates selection leads to severe performance downgrades due to the coordinate constraints becoming hard to satisfy for the solver
COORDINATE_CONSTRAINTS = [
    MiniZincB("Models/Minizinc/Stones matrix/Testing constraint choice/indomain_min.mzn", "without coordinates constraints", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/input_order indomain_min.mzn", "with coordinates constraints", TOTAL_TIME_BUDGET_PER_SOLVER),
]

TESTING_CONSTRAINT_CHOICE = [
    MiniZincB("Models/Minizinc/Stones matrix/Testing constraint choice/indomain_interval.mzn", "indomain_interval", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Stones matrix/Testing constraint choice/indomain_min.mzn", "indomain_min", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Stones matrix/Testing constraint choice/indomain_random.mzn", "indomain_random", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Stones matrix/Testing constraint choice/indomain_split.mzn", "indomain_split", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Stones matrix/Testing constraint choice/outdomain_max.mzn", "outdomain_max", TOTAL_TIME_BUDGET_PER_SOLVER),
]

PRELIMINARY_BATCH_TEST = [
    MiniZincB("Models/Minizinc/Stones matrix/Testing variable choice/Basic dom_w_deg.mzn", "new dom_w_deg", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Stones matrix/Testing variable choice/Basic first_fail.mzn", "new first_fail", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Stones matrix/Testing variable choice/Basic most_constrained.mzn", "new most_constrained", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Stones matrix/Testing variable choice/Basic max_regret.mzn", "new max_regret", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincA("Models/Minizinc/Old/Basic dom_w_deg.mzn", "old dom_w_deg", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincA("Models/Minizinc/Old/Basic first_fail.mzn", "old first_fail", TOTAL_TIME_BUDGET_PER_SOLVER),
]

BASIC_BATCHES = [
    TestBatch(
        "Trivial",
        n=5,
        tilecount=15,
        reps=20
    ),
    TestBatch(
        "Easy",
        n=10,
        tilecount=60,
        reps=10
    ),
    TestBatch(
        "Medium",
        n=11,
        tilecount=100,
        reps=4
    ),
    TestBatch(
        "Hard",
        n=12,
        tilecount=90,
        reps=2
    ),
    TestBatch(
        "Extreme",
        n=15,
        tilecount=120,
        reps=1
    )
]

HARD_BATCHES = [
    TestBatch(
        "Trivial",
        n=10,
        tilecount=60,
        reps=20
    ),
    TestBatch(
        "Easy",
        n=18,
        tilecount=180,
        reps=10
    ),
    TestBatch(
        "Medium",
        n=25,
        tilecount=340,
        reps=5
    ),
    TestBatch(
        "Hard",
        n=30,
        tilecount=470,
        reps=3
    ),
    TestBatch(
        "Very Hard",
        n=33,
        tilecount=560,
        reps=2
    ),
    TestBatch(
        "Extreme",
        n=40,
        tilecount=850,
        reps=1
    )
]

EXTREME_BATCHES = [
    TestBatch(
        "Restricted tiles",
        n=33,
        tilecount=548,
        reps=2
    ),
    TestBatch(
        "Very Hard",
        n=33,
        tilecount=600,
        reps=3
    ),
    TestBatch(
        "Extreme",
        n=40,
        tilecount=850,
        reps=2
    ),
    TestBatch(
        "Uber",
        n=50,
        tilecount=1375,
        reps=2
    )
]

SOLVERS = KEEP_CHANCE_B

BATCHES = EXTREME_BATCHES

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