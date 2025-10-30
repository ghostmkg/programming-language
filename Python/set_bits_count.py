"""
Problem:
Given an integer, count how many 1s are present in its binary representation.

Example:
Input: 13 (1101) → Output: 3
"""

def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count