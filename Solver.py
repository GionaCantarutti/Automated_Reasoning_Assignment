import StonesInstance

class Solver:

    def tBudget_left(self):
        return self.time_budget
    
    def spend_time(self, spent):
        self.time_budget -= spent

    #Name of the solver
    def label(self):
        return self.name

    #Timeout given in seconds
    def solveInstance(self, instance: StonesInstance, timeout):
        #Solve and add the solution to the instance, then return it
        pass