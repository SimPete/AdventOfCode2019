### Day3 - Wires Crossing

import numpy
from lib import Day3_fct

### CREATING THE GRID
nb_lines = 40
nb_columns = 40
GRID = numpy.zeros((nb_lines,nb_columns),dtype = int)

# print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
      # for row in GRID]))

### FINDING THE CENTER
center_of_lines = int(nb_lines/2)
center_of_columns = int(nb_columns/2)
GRID[center_of_lines,center_of_columns] = 1
current_position=(center_of_lines, center_of_columns)

print(current_position)

### IMPORT THE WIRES DATA
input = open('./ressources/Day3_Test1.txt','r')
Wire1 = input.readline().split(',')
Wire2 = input.readline().split(',')
input.close()
print(Wire1)
print(Wire2)

### DRAW THE FIRST WIRE
for i in range((len(Wire1))):  
    Dir=Wire1[i][0] #Direction
    Steps=Wire1[i][1] #Number of steps
    print(Dir, Steps)
    
    # Walk the steps in the direction
    for s in range(int(Steps)):
        GRID[int(nb_lines/2),int(nb_columns/2)] = 1


# Day3_fct.gridprint(GRID)