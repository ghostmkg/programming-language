MOD = 10**9 + 7

def mazeObstacles(m, n, obstacleGrid):
    dp = [[0] * n for _ in range(m)]
    
   
    if obstacleGrid[0][0] == 1:
        return 0
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0  
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD
    
    return dp[m-1][n-1] % MOD

# Example usage:
m = 3
n = 3
obstacleGrid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(mazeObstacles(m, n, obstacleGrid))  # Output: 2
# time complexity: O(m*n)
# space complexity: O(m*n)