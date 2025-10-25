"""
Problem:
Given an array containing n distinct numbers from 0 to n, find the missing number.

Example:
Input: [3, 0, 1] → Output: 2
"""
def missing_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    return total - sum(nums)