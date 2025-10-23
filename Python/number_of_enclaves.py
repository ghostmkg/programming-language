"""
You are given an n x m binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4- directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example
Input:
4 4
0 0 0 0
1 0 1 0
0 1 1 0
0 0 0 0
Output:
3
"""


def numEnclaves(grid):
    assert grid and grid[0], "Grid must not be empty"
    rows, cols = len(grid), len(grid[0])
    assert 1 <= rows <= 10**4 and 1 <= cols <= 10**4 and rows * cols <= 10**4, "Grid dimensions out of bounds"
    for row in grid:
        assert len(row) == cols, "Grid must be rectangular"
        for cell in row:
            assert cell in (0, 1), "Grid values must be 0 or 1"

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dfs(x, y):
        if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0:
            return
        grid[x][y] = 0
        for dx, dy in directions:
            dfs(x + dx, y + dy)

    for i in range(rows):
        if grid[i][0] == 1:
            dfs(i, 0)
        if grid[i][cols - 1] == 1:
            dfs(i, cols - 1)

    for j in range(cols):
        if grid[0][j] == 1:
            dfs(0, j)
        if grid[rows - 1][j] == 1:
            dfs(rows - 1, j)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                count += 1
    return count
