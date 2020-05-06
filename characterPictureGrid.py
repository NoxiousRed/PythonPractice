grid = [['.', '.', '.', '.', '.', '.'],
       ['.', 'O', 'O', '.', '.', '.'],
       ['O', 'O', 'O', 'O', '.', '.'],
       ['O', 'O', 'O', 'O', 'O', '.'],
       ['.', 'O', 'O', 'O', 'O', 'O'],
       ['O', 'O', 'O', 'O', 'O', '.'],
       ['O', 'O', 'O', 'O', '.', '.'],
       ['.', 'O', 'O', '.', '.', '.'],
       ['.', '.', '.', '.', '.', '.']]

def gridOutput(grid):
    for s in range(len(grid[0])):
        print()
        for i in range(len(grid)):
            print(grid[i][s],end='')
gridOutput(grid)