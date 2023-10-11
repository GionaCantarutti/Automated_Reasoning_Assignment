import minizinc as mzn
import pathlib
import random as r
import datetime

timeOutSeconds = 40

localPath = str(pathlib.Path(__file__).parent.resolve())

model1 = mzn.Model()
model1.add_file(localPath + "\Stones2.mzn")

model2 = mzn.Model()
model2.add_file(localPath + "\Stones3.mzn")

gecode = mzn.Solver.lookup("gecode")

def solve1(s, n):
    inst = mzn.Instance(gecode, model1)

    inst["n"] = n
    inst["t"] = len(s)
    inst["Stones"] = s

    return inst.solve()

def solve2(s, n):
    return None

def optimize1(s, n):
    inst = mzn.Instance(gecode, model1)

    inst["n"] = n
    inst["t"] = len(s)
    inst["Stones"] = s 

    return inst.solve(intermediate_solutions=True, timeout=datetime.timedelta(seconds=timeOutSeconds))

def optimize2(s, n):
    inst = mzn.Instance(gecode, model2)

    inst["n"] = n
    inst["Stones"] = stoneListToStoneMatrix(s)

    return inst.solve(intermediate_solutions=True, timeout=datetime.timedelta(seconds=timeOutSeconds))

def stoneListToStoneMatrix(stoneList):
    stoneMatrix = [[0 for x in range(7)] for y in range(7)]
    for s in stoneList:
        stoneMatrix[s[0]][s[1]] += 1
        stoneMatrix[s[1]][s[0]] += 1

    return stoneMatrix

def formatSolution2(stoneList, n, placements, coordinates):
    newPlacements = []
    sides = []

    for p in placements:
        for i in range(len(stoneList)):
            if (p[0] == stoneList[i][0] & p[1] == stoneList[i][1]):
                newPlacements.append(i+1)
                sides.append(0)
            elif (p[1] == stoneList[i][0] & p[0] == stoneList[i][1]):
                newPlacements.append(i+1)
                sides.append(1)

    for i in range(len(newPlacements), n**2):
        newPlacements.append(0)
        sides.append(0)
    
    return formatSolution1(stoneList, n, newPlacements, coordinates, sides)


def formatSolution1(stones, n, placements, coordinates, sides):
    grid = [[[0 for x in range(n)] for y in range(n)] for z in range(2)]

    for i in range(n**2):
        if (placements[i] != 0):
            grid[0][coordinates[0][i]-1][coordinates[1][i]-1] = placements[i]
            grid[1][coordinates[0][i]-1][coordinates[1][i]-1] = sides[i]

    solutionGrid = ""

    for i in range(0, n):
        for j in range(0, n):
            if (grid[0][i][j] == 0):
                solutionGrid += "#"
            else:
                solutionGrid += str(stones[grid[0][i][j]-1][grid[1][i][j]-1])
            if (j < n-1):
                if (grid[0][i][j] == grid[0][i][j+1]):
                    solutionGrid += "-"
                else:
                    solutionGrid += "|"
        solutionGrid += "\n"
        for j in range(0,n):
            if (i < n-1):
                if (grid[0][i][j] == grid[0][i+1][j]):
                    solutionGrid += "| "
                else:
                    solutionGrid += "  "
        solutionGrid += "\n"
    
    return solutionGrid

def solveAndPrint1(s, n, modeln):
    
    if (modeln == 1):
        result = solve1(s,n)
    else:
        result = solve2(s,n)

    placements = result.__getitem__("Placements")
    coordinates = result.__getitem__("Coordinates")
    sides = result.__getitem__("Sides")

    print(formatSolution1(s, n, placements, coordinates, sides))

    

def solveRandom1(size, tileCount):
    st = []
    for i in range(tileCount):
        st.append((r.randint(0,6),r.randint(0,6)))
    solveAndPrint1(st, size)

def optimizeRandom(size, tileCount, modeln):
    st = []
    for i in range(tileCount):
        st.append((r.randint(0,6),r.randint(0,6)))

    if (modeln == 1):
        solutions = optimize1(st, size)
    elif (modeln == 2):
        solutions = optimize2(st, size)

    if (modeln == 1):
        for i in range(solutions.__len__()):
            placements = solutions.__getitem__((i, "Placements"))
            coordinates = solutions.__getitem__((i, "Coordinates"))
            sides = solutions.__getitem__((i, "Sides"))
            print(formatSolution1(st, size, placements, coordinates, sides))
            print("Empty spaces left: " + str(solutions.__getitem__(i).objective) + " of a minimum of " + str(max(size**2 - len(st)*2,0)))
            print("___________________________")
    elif (modeln == 2):
        for i in range(solutions.__len__()):
            placements = solutions.__getitem__((i, "Placements"))
            coordinates = solutions.__getitem__((i, "Coordinates"))
            print(formatSolution2(st, size, placements, coordinates))
            print("Empty spaces left: " + str(solutions.__getitem__(i).objective) + " of a minimum of " + str(max(size**2 - len(st)*2,0)))
            print("___________________________")
            


    if solutions.__len__() > 0:
        print("Took a total of: " + str(solutions.statistics["solveTime"].seconds
                                        + solutions.statistics["solveTime"].microseconds/1000000
                                        + solutions.statistics["flatTime"].seconds
                                        + solutions.statistics["flatTime"].microseconds/1000000) + " seconds")
        print("Of which " + str(solutions.statistics["solveTime"].seconds
                                        + solutions.statistics["solveTime"].microseconds/1000000) + " spent solving and "
                                        + str(solutions.statistics["flatTime"].seconds
                                        + solutions.statistics["flatTime"].microseconds/1000000) + " spent flattening")
    else:
        print("Found no solutions in time")

#solveRandom(7, 14)
#optimizeRandom(9,1000)

optimizeRandom(5, 10, 2)