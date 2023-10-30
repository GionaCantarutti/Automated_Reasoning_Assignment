from MiniZincA import *
from MiniZincB import *

TOTAL_TIME_BUDGET_PER_SOLVER = 13 * 5 * 60

FINAL_TESTING = [
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 15 conditional.mzn", "dom_w_deg + indomain_min", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Final models/dom_w_deg + indomain_random.mzn", "dom_w_deg + indomain_random", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Final models/dom_w_deg + indomain_split.mzn", "dom_w_deg + indomain_split", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Final models/input_order + indomain_min.mzn", "input_order + indomain_min", TOTAL_TIME_BUDGET_PER_SOLVER),
]

KEEP_CHANCE_D = [
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 15 conditional.mzn", "luby 15", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 15 full scale.mzn", "luby 15 full scale", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 25 conditional.mzn", "luby 25", TOTAL_TIME_BUDGET_PER_SOLVER),
]

KEEP_CHANCE_C = [
    MiniZincB("Models/Minizinc/Improved coordinates/prevent zigzag.mzn", "no restart", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 5 conditional.mzn", "luby 5", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 10 conditional.mzn", "luby 10", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 15 conditional.mzn", "luby 15", TOTAL_TIME_BUDGET_PER_SOLVER),
]

#Seemingly unfixable, cannot use non-fixed variables in relax_and_reconstruct :(
NONPLACEMENT_FIX = [
    MiniZincB("Models/Minizinc/Improved coordinates/prevent zigzag.mzn", "no restart", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 50 nonplacements fix.mzn", "luby 50 fixed", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 50.mzn", "luby 50 not fixed", TOTAL_TIME_BUDGET_PER_SOLVER),
]

KEEP_CHANCE_B = [
    MiniZincB("Models/Minizinc/Improved coordinates/prevent zigzag.mzn", "no restart", TOTAL_TIME_BUDGET_PER_SOLVER),
    MiniZincB("Models/Minizinc/Improved coordinates/Keep chance/luby 15.mzn", "luby 15", TOTAL_TIME_BUDGET_PER_SOLVER),
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