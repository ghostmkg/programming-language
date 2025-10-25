def maxSum(n,nums):
    dp=[0]*n
    dp[0]=nums[0]
    for i in range(1,n):
        ans=nums[i]
        if i>1:
            ans+=dp[i-2]
        notans=dp[i-1]
        dp[i]=max(ans,notans)
    return dp[-1]

n=int(input())
nums=list(map(int,input().split()))
print(maxSum(n,nums))
# Function to find the maximum sum of non-adjacent numbers in a list
# using dynamic programming approach