### Day3 - Wires Crossing

import numpy
from lib import Day3_fct

### CREATING THE GRID
nb_lines = 40
nb_columns = 40
crossingFound = 0
wire1Symbol=5
wire2Symbol=8
wireCrossingSymbol=7
GRID = numpy.zeros((nb_lines,nb_columns),dtype = int)

# print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      # for row in GRID]))

### FINDING THE CENTER
center_of_lines = int(nb_lines/2)
center_of_columns = int(nb_columns/2)
GRID[center_of_lines,center_of_columns] = 1
startingPosition=(center_of_lines, center_of_columns)
crossing=[]

print("Current position is : ", startingPosition)

### IMPORT THE WIRES DATA
input = open('./ressources/Day3_Test1.txt','r')
Wire1 = input.readline().split(',')
Wire2 = input.readline().split(',')
input.close()
print(Wire1)
print(Wire2)

### DRAW THE FIRST WIRE
currentPosition=startingPosition #Reset currentPosition to center
for command in range((len(Wire1))): 
    dir=Wire1[command][0] #direction
    steps=Wire1[command][1] #Number of steps
    print(dir, steps)
    
    if dir == "U":
        for step in range(int(steps)):
            currentPosition=(currentPosition[0]-1, currentPosition[1])
            GRID[currentPosition] = wire1Symbol
    elif dir == "D":
        for step in range(int(steps)):
            currentPosition=(currentPosition[0]+1, currentPosition[1])
            GRID[currentPosition] = wire1Symbol
    elif dir == "L":
        for step in range(int(steps)):
            currentPosition=(currentPosition[0], currentPosition[1]-1)
            GRID[currentPosition] = wire1Symbol
    elif dir  == "R":
        for step in range(int(steps)):
            currentPosition=(currentPosition[0], currentPosition[1]+1)
            GRID[currentPosition] = wire1Symbol
    else :
        print("FATAL ERROR: Unsupported direction received")

### DRAW THE SECOND WIRE
currentPosition=startingPosition #Reset currentPosition to center
for command in range((len(Wire2))): 
    dir=Wire2[command][0] #direction
    steps=Wire2[command][1] #Number of steps
    print(dir, steps)
    
    if dir == "U":
        for step in range(int(steps)):
            currentPosition=(currentPosition[0]-1, currentPosition[1])
            if GRID[currentPosition] == wire1Symbol:
                crossingFound+=1
                print("CROSSING FOUND! Crossing found count is now : ", crossingFound)
                crossing.append(currentPosition)
                GRID[currentPosition] = wireCrossingSymbol
            else:
                GRID[currentPosition] = wire2Symbol
    elif dir == "D":
        for step in range(int(steps)):
            currentPosition=(currentPosition[0]+1, currentPosition[1])
            if GRID[currentPosition] == wire1Symbol:
                crossingFound+=1
                print("CROSSING FOUND! Crossing found count is now : ", crossingFound)
                crossing.append(currentPosition)
                GRID[currentPosition] = wireCrossingSymbol
            else:
                GRID[currentPosition] = wire2Symbol
    elif dir == "L":
        for step in range(int(steps)):
            currentPosition=(currentPosition[0], currentPosition[1]-1)
            if GRID[currentPosition] == wire1Symbol:
                crossingFound+=1
                print("CROSSING FOUND! Crossing found count is now : ", crossingFound)
                crossing.append(currentPosition)
                GRID[currentPosition] = wireCrossingSymbol
            else:
                GRID[currentPosition] = wire2Symbol
    elif dir  == "R":
        for step in range(int(steps)):
            currentPosition=(currentPosition[0], currentPosition[1]+1)
            if GRID[currentPosition] == wire1Symbol:
                crossingFound+=1
                print("CROSSING FOUND! Crossing found count is now : ", crossingFound)
                crossing.append(currentPosition)
                GRID[currentPosition] = wireCrossingSymbol
            else:
                GRID[currentPosition] = wire2Symbol
    else :
        print("FATAL ERROR: Unsupported direction received")
        
Day3_fct.gridprint(GRID)
print("Crossing points found are : ", crossing)

print('anything')




