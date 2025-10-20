dp = {}
def uniquePaths(m , n):
    if m == 1 and n == 1:
        return 1
    if m < 1 or n < 1:
        return 0
    if (m, n) in dp:
        return dp[(m, n)]
    dp[(m, n)] = uniquePaths(m - 1, n) + uniquePaths(m, n - 1)
    return dp[(m, n)]

print(uniquePaths(3, 7))  # Output: 28
# The function uniquePaths calculates the number of unique paths
# from the top-left corner to the bottom-right corner of an m x n grid.
# You can only move either down or right at any point in time.