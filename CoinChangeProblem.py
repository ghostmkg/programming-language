def coin_change(coins, amount):
    # Initialize a list to store the minimum coins for each amount from 0 to amount
    dp = [float('inf')] * (amount + 1)
    
    # Base case: to make 0 amount, 0 coins are needed
    dp[0] = 0
    
    # Iterate over each coin in the coins list
    for coin in coins:
        # For each coin, update the dp array for all amounts from coin to amount
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still infinity, that means it's not possible to form that amount
    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 11
result = coin_change(coins, amount)
print(f"Minimum coins needed: {result}")
