grid =       [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]


newgrid = [[x[i] for x in grid] for i in range(len(grid[0]))]
print (newgrid)