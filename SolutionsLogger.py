import numpy as np
import os

class SolutionsLogger:

    def open_logfile(dirPath):
        file = open(os.path.join(dirPath, "solutions.txt"), "a")
        return file

    def make_log_string(StonesInstance):

        string = "\n"
        string += "#############################################\n"
        string += "Solver " + StonesInstance.solution.solverUsed + " on instance of size " + str(StonesInstance.n) + " with stones:\n"
        string += str(StonesInstance.stones) + "\n\n"

        if StonesInstance.solution.objective is not None:
            string += "Solution with cost " + str(StonesInstance.solution.objective) + ":\n"
            string += StonesInstance.solutionString() + "\n"
        else:
            string += "No solution was found in time\n"

        totalSolve = StonesInstance.solution.solveTime.seconds + StonesInstance.solution.solveTime.microseconds/1000000
        totalFlat = StonesInstance.solution.flatTime.seconds + StonesInstance.solution.flatTime.microseconds/1000000
        totalTime = totalSolve + totalFlat

        string += "Took a total of " + str(totalTime) + ", of which " + str(totalSolve) + " spent solving and " + str(totalFlat) + " spent flattening\n"

        return string
    
    def log_new(StonesInstance, file):
        file.write(SolutionsLogger.make_log_string(StonesInstance))

    def close_logfile(file):
        file.close()