def orangesRotting(grid):
    n,m = len(grid),len(grid[0])

    move = [[1,0],[-1,0],[0,1],[0,-1]]
    time = -1
    q = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append([i,j,0])
    
    while q:
        a = q.pop(0)
        time = a[2]

        for direc in move:
            x,y = a[0]+direc[0],a[1]+direc[1]
            if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                q.append([x,y,a[2]+1])
                grid[x][y] = 2
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                return -1
    return time