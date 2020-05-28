def travel(Dir, Steps, Current_Position):
    for s in range(int(Steps)):
        GRID[int(nb_lines/2),int(nb_columns/2)] = 1


    return Current_Position
    
def gridprint(GRID):
    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
        for row in GRID]))