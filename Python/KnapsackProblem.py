# Function to solve the 0/1 Knapsack Problem
def knapsack(weights, values, capacity):
    # Number of items
    n = len(values)
    
    # Create a 2D DP array where dp[i][w] represents the maximum value that can be obtained
    # with the first i items and a knapsack of capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:  # Can include this item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:  # Can't include this item
                dp[i][w] = dp[i - 1][w]
    
    # The maximum value is in dp[n][capacity]
    return dp[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = knapsack(weights, values, capacity)
print(f"Maximum value in the knapsack: {max_value}")
