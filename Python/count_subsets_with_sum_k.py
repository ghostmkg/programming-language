def findWays(nums, k):
    MOD = 10**9 + 7
    n = len(nums)

    dp = [0] * (k + 1)
    dp[0] = 1   # There is always 1 way to make sum = 0 (choose nothing)

    for num in nums:
        # Iterate backwards to avoid reusing the same element twice
        for target in range(k, num - 1, -1):
            dp[target] = (dp[target] + dp[target - num]) % MOD

    return dp[k]