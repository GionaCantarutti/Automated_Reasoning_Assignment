import os

class StatisticsLogger:

    FILE_NAME = "statistics.txt"

    def __init__(self, batchFileName, n, stoneCount, solverName, single_timeout):
        self.samples = 0
        self.cumulativeTime = 0
        self.cumulativeCost = 0
        self.size = n
        self.stoneCount = stoneCount
        self.timed_out = False   #Means that the solver ran out of total time
        self.single_timeout = single_timeout

        self.solver = solverName
        self.file_name = batchFileName
        
    def init_file(path):
        file = open(os.path.join(path, StatisticsLogger.FILE_NAME), "a")
        file.write("solver,n,stones,avgTime,avgCost,samples,ran_out_of_time,single_timeout")
        StatisticsLogger.close_file(file)

    def open_file(path):
        file = open(os.path.join(path, StatisticsLogger.FILE_NAME), "a")
        return file
    
    def close_file(file):
        file.close()
    
    def add_data(self, instance):
        self.samples += 1
        self.cumulativeTime += instance.solution.solveTime.seconds + instance.solution.flatTime.seconds + (instance.solution.solveTime.microseconds + instance.solution.flatTime.microseconds)/1000000
        self.cumulativeCost += instance.solution.objective

    def log_timeout(self):
        self.timed_out = True

    def make_data_string(self):
        if self.samples > 0:
            avgTime = self.cumulativeTime / self.samples
            avgCost = self.cumulativeCost / self.samples
        else:
            avgTime = -1
            avgCost = -1
        return "\n" + self.solver + "," + str(self.size) + "," + str(self.stoneCount) + "," + str(avgTime) + "," + str(avgCost) + "," + str(self.samples) + "," + str(self.timed_out) + "," + str(self.single_timeout)

    def reset(self):
        self.samples = -1
        self.cumulativeTime = -1
        self.size = 0
        self.stoneCount = 0
        self.timed_out = False
        self.file_name = ""

    def createName(solver, batch):
        return solver.label() + "_solver_on_" + batch.label + "_batch.txt"

    def log_line(self, file):
        
        file.write(self.make_data_string())

        self.reset()