from StonesInstance import StoneInstance
from MiniZincA import MiniZincA
from MiniZincB import MiniZincB
from TestBatch import TestBatch
from SolutionsLogger import SolutionsLogger
from StatisticsLogger import StatisticsLogger

TIMEOUT = 5 * 60
TOTAL_TIME_BUDGET_PER_SOLVER = 15 * 60

SOLVERS = [
    MiniZincA("Stones2.mzn", "old", TOTAL_TIME_BUDGET_PER_SOLVER), 
    MiniZincB("Stones3.mzn", "new", TOTAL_TIME_BUDGET_PER_SOLVER),
    ]

BATCHES = [
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
        reps=2
    ),
    TestBatch(
        "Hard",
        n=15,
        tilecount=120,
        reps=1
    )
]

log_file = SolutionsLogger.init_logfile()

stats = [[StatisticsLogger(StatisticsLogger.createName(solver, batch), batch.size, batch.tilecount, solver.label(), TIMEOUT) for solver in SOLVERS] for batch in BATCHES]

for bi, batch in enumerate(BATCHES):
    for i in range(batch.repetitions):
        newInstance = StoneInstance.generateRandom(batch.size, batch.tilecount)
        for si, solver in enumerate(SOLVERS):

            if solver.tBudget_left() <= 0:
                print(solver.label() + " solver ran out of time, moving on")
                stats[bi][si].log_timeout()
                continue

            print(batch.label + " batch with " + solver.label() + " solver, repetition " + str(i) + "/" + str(batch.repetitions) + " ...")
            
            solved = solver.solveInstance(newInstance, min(solver.tBudget_left(), TIMEOUT))
            solver.spend_time(solved.solution.solveTime.seconds + solved.solution.flatTime.seconds)

            SolutionsLogger.log_new(solved, log_file)
            stats[bi][si].add_data(solved)

    for j in range(len(SOLVERS)):
        stats[bi][j].close_and_save("stats/")
        
print("DONE!")

#MiniZincB performa molto meglio quando gli vengono date abbastanza tiles. Oltre ad un certo punto aumentare le tiles smette di avere un costo sulla performance
#MiniZincB andrà in timeout per n=11 con 70 tiles (poco più del minimo necessario per coprire la grid) ma riesce a risolvere l'istanza n11 con 120 tiles in soli 25 secondi
#MiniZincA probabilmente non funziona alla stessa maniera, da testare

#newInstance = StoneInstance.generateRandom(EASY_SIZE, EASY_TILECOUNT)
#solverB = MiniZincB("Stones3.mzn")
#print((solverB.solveInstance(newInstance, TIMEOUT)).solutionString())