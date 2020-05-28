def gridprint(GRID):
    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) 
        for row in GRID]))