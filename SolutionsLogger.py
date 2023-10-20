import numpy as np

class SolutionsLogger:

    def init_logfile():
        return "test_log.txt"

    def make_log_string(StonesInstance):

        string = "\n"
        string += "#############################################\n"
        string += "Solver " + StonesInstance.solution.solverUsed + " on instance of size " + str(StonesInstance.n) + " with stones:\n"
        string += str(StonesInstance.stones) + "\n\n"

        string += "Solution with cost " + str(StonesInstance.solution.objective) + ":\n"
        string += StonesInstance.solutionString() + "\n"

        totalSolve = StonesInstance.solution.solveTime.seconds + StonesInstance.solution.solveTime.microseconds/1000000
        totalFlat = StonesInstance.solution.flatTime.seconds + StonesInstance.solution.flatTime.microseconds/1000000
        totalTime = totalSolve + totalFlat

        string += "Took a total of " + str(totalTime) + ", of which " + str(totalSolve) + " spent solving and " + str(totalFlat) + " spent flattening\n"

        return string
    
    def log_new(StonesInstance, path):
        print(SolutionsLogger.make_log_string(StonesInstance))