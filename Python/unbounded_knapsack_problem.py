def getMaximumValue(weights, values, n, maxWeight):
    dp = [0] * (maxWeight + 1)

    for w in range(1, maxWeight + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[maxWeight]