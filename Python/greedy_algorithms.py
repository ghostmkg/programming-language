"""
Greedy Algorithms Implementation
=================================

Collection of classic greedy algorithms including activity selection,
Huffman coding, job scheduling, and fractional knapsack.

Author: Hacktoberfest 2025 Contributor
"""

import heapq
from typing import List, Tuple
from collections import defaultdict


class GreedyAlgorithms:
    """Collection of greedy algorithm implementations"""
    
    @staticmethod
    def activity_selection(start: List[int], finish: List[int]) -> List[int]:
        """
        Activity Selection Problem
        Select maximum number of non-overlapping activities
        
        Time: O(n log n)
        Space: O(n)
        """
        activities = [(finish[i], start[i], i) for i in range(len(start))]
        activities.sort()
        
        selected = [activities[0][2]]
        last_finish = activities[0][0]
        
        for finish_time, start_time, index in activities[1:]:
            if start_time >= last_finish:
                selected.append(index)
                last_finish = finish_time
        
        return selected
    
    @staticmethod
    def fractional_knapsack(values: List[int], weights: List[int], 
                           capacity: int) -> float:
        """
        Fractional Knapsack Problem
        
        Time: O(n log n)
        Space: O(n)
        """
        # Calculate value per unit weight
        items = [(values[i] / weights[i], values[i], weights[i]) 
                 for i in range(len(values))]
        items.sort(reverse=True)
        
        total_value = 0.0
        remaining_capacity = capacity
        
        for ratio, value, weight in items:
            if remaining_capacity >= weight:
                total_value += value
                remaining_capacity -= weight
            else:
                total_value += ratio * remaining_capacity
                break
        
        return total_value
    
    @staticmethod
    def job_sequencing(jobs: List[Tuple[str, int, int]]) -> Tuple[List[str], int]:
        """
        Job Sequencing with Deadlines
        
        Time: O(n^2)
        Space: O(n)
        
        Args:
            jobs: List of (job_id, deadline, profit)
        Returns:
            (selected_jobs, total_profit)
        """
        # Sort jobs by profit (descending)
        jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
        
        max_deadline = max(job[1] for job in jobs)
        slots = [None] * max_deadline
        total_profit = 0
        selected_jobs = []
        
        for job_id, deadline, profit in jobs:
            # Find a free slot before deadline
            for slot in range(min(deadline, max_deadline) - 1, -1, -1):
                if slots[slot] is None:
                    slots[slot] = job_id
                    selected_jobs.append(job_id)
                    total_profit += profit
                    break
        
        return selected_jobs, total_profit
    
    @staticmethod
    def huffman_coding(text: str) -> dict:
        """
        Huffman Coding for data compression
        
        Time: O(n log n)
        Space: O(n)
        
        Returns: Dictionary mapping characters to binary codes
        """
        # Count frequency
        freq = defaultdict(int)
        for char in text:
            freq[char] += 1
        
        # Build Huffman tree using min heap
        heap = [[weight, [char, ""]] for char, weight in freq.items()]
        heapq.heapify(heap)
        
        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        
        # Extract codes
        codes = {char: code for char, code in heap[0][1:]}
        return codes
    
    @staticmethod
    def minimum_platforms(arrivals: List[int], departures: List[int]) -> int:
        """
        Minimum Railway Platforms Problem
        
        Time: O(n log n)
        Space: O(1)
        """
        arrivals.sort()
        departures.sort()
        
        platforms_needed = 0
        max_platforms = 0
        i = j = 0
        
        while i < len(arrivals):
            if arrivals[i] < departures[j]:
                platforms_needed += 1
                max_platforms = max(max_platforms, platforms_needed)
                i += 1
            else:
                platforms_needed -= 1
                j += 1
        
        return max_platforms
    
    @staticmethod
    def coin_change_greedy(coins: List[int], amount: int) -> List[int]:
        """
        Coin Change using Greedy (works for canonical coin systems)
        
        Time: O(n)
        Space: O(1)
        
        Note: Greedy doesn't always give optimal solution
        """
        coins.sort(reverse=True)
        result = []
        
        for coin in coins:
            while amount >= coin:
                result.append(coin)
                amount -= coin
        
        return result if amount == 0 else []
    
    @staticmethod
    def minimize_sum_of_products(a: List[int], b: List[int]) -> int:
        """
        Minimize sum of products by rearranging arrays
        
        Time: O(n log n)
        Space: O(1)
        """
        a.sort()
        b.sort(reverse=True)
        
        return sum(a[i] * b[i] for i in range(len(a)))
    
    @staticmethod
    def connect_ropes(ropes: List[int]) -> int:
        """
        Connect n ropes with minimum cost
        Cost to connect two ropes = sum of their lengths
        
        Time: O(n log n)
        Space: O(n)
        """
        heapq.heapify(ropes)
        total_cost = 0
        
        while len(ropes) > 1:
            first = heapq.heappop(ropes)
            second = heapq.heappop(ropes)
            
            cost = first + second
            total_cost += cost
            
            heapq.heappush(ropes, cost)
        
        return total_cost
    
    @staticmethod
    def buy_sell_stock_once(prices: List[int]) -> int:
        """
        Maximum profit from buying and selling stock once
        
        Time: O(n)
        Space: O(1)
        """
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        
        return max_profit
    
    @staticmethod
    def buy_sell_stock_multiple(prices: List[int]) -> int:
        """
        Maximum profit from multiple transactions
        
        Time: O(n)
        Space: O(1)
        """
        total_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i - 1]
        
        return total_profit


# Demonstration
def demonstrate_greedy_algorithms():
    print("=" * 70)
    print("GREEDY ALGORITHMS DEMONSTRATION")
    print("=" * 70)
    
    algo = GreedyAlgorithms()
    
    # Activity Selection
    print("\n1. ACTIVITY SELECTION")
    start = [1, 3, 0, 5, 8, 5]
    finish = [2, 4, 6, 7, 9, 9]
    selected = algo.activity_selection(start, finish)
    print(f"   Start times: {start}")
    print(f"   Finish times: {finish}")
    print(f"   Selected activities: {selected}")
    print(f"   Maximum activities: {len(selected)}")
    
    # Fractional Knapsack
    print("\n2. FRACTIONAL KNAPSACK")
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    max_value = algo.fractional_knapsack(values, weights, capacity)
    print(f"   Values: {values}")
    print(f"   Weights: {weights}")
    print(f"   Capacity: {capacity}")
    print(f"   Maximum value: {max_value:.2f}")
    
    # Job Sequencing
    print("\n3. JOB SEQUENCING")
    jobs = [
        ("J1", 2, 100),
        ("J2", 1, 19),
        ("J3", 2, 27),
        ("J4", 1, 25),
        ("J5", 3, 15)
    ]
    selected_jobs, profit = algo.job_sequencing(jobs)
    print(f"   Jobs: {[(j[0], f'D:{j[1]}', f'P:{j[2]}') for j in jobs]}")
    print(f"   Selected: {selected_jobs}")
    print(f"   Total profit: {profit}")
    
    # Huffman Coding
    print("\n4. HUFFMAN CODING")
    text = "AAABBC"
    codes = algo.huffman_coding(text)
    print(f"   Text: {text}")
    print(f"   Huffman codes: {codes}")
    original_size = len(text) * 8
    encoded_size = sum(len(codes[char]) for char in text)
    print(f"   Compression: {original_size} bits → {encoded_size} bits")
    
    # Minimum Platforms
    print("\n5. MINIMUM RAILWAY PLATFORMS")
    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]
    platforms = algo.minimum_platforms(arrivals, departures)
    print(f"   Arrivals: {arrivals}")
    print(f"   Departures: {departures}")
    print(f"   Minimum platforms needed: {platforms}")
    
    # Coin Change
    print("\n6. COIN CHANGE (GREEDY)")
    coins = [1, 5, 10, 25]
    amount = 41
    result = algo.coin_change_greedy(coins.copy(), amount)
    print(f"   Coins: {coins}")
    print(f"   Amount: {amount}")
    print(f"   Coins used: {result}")
    
    # Connect Ropes
    print("\n7. CONNECT ROPES")
    ropes = [4, 3, 2, 6]
    cost = algo.connect_ropes(ropes.copy())
    print(f"   Rope lengths: {[4, 3, 2, 6]}")
    print(f"   Minimum cost: {cost}")
    
    # Stock Trading
    print("\n8. STOCK TRADING")
    prices = [7, 1, 5, 3, 6, 4]
    profit_once = algo.buy_sell_stock_once(prices)
    profit_multiple = algo.buy_sell_stock_multiple(prices)
    print(f"   Prices: {prices}")
    print(f"   Max profit (1 transaction): {profit_once}")
    print(f"   Max profit (multiple): {profit_multiple}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    demonstrate_greedy_algorithms()
