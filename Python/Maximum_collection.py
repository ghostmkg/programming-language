def max_coins(grid):
    dp = {}
    m = len(grid)
    n = len(grid[0])
    ans = helper(m, n, grid, dp)
    return ans

def helper(m, n, grid, dp):
    if m == 1 and n == 1:
        return grid[0][0]
    if m < 0 or n < 0:
        return float('-inf')
    if (m, n) in dp:
        return dp[(m, n)]
    dp[(m, n)] = grid[m - 1][n - 1] + max(helper(m - 1, n, grid, dp), helper(m, n - 1, grid, dp))
    return dp[(m, n)]


print(max_coins([[0, 3, 1, 1], [2, 0, 0, 4], [1, 0, 0, 0], [5, 0, 0, 0]]))  # Output: 12
# The function max_coins calculates the maximum number of coins that can be collected
# while moving from the top-left corner to the bottom-right corner of the grid.
# You can only move either down or right at any point in time.
