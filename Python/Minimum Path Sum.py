def minPathSum(grid):
    m=len(grid)
    n=len(grid[0])
    memo={}
    def helper(i,j):
        if (i,j) in memo:
            return memo[(i,j)]
        if i==m-1 and j==n-1:
            return grid[i][j]
        if i>=m or j>=n:
            return float('inf')
        case1=helper(i+1,j)+grid[i][j]
        case2=helper(i,j+1)+grid[i][j]
        ans=min(case1,case2)
        memo[(i,j)]=ans 
        return ans
    return helper(0,0)