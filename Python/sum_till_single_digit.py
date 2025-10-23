"""
Problem:
Keep summing digits of a number until you get a single digit.

Example:
Input: 9875
9+8+7+5=29
2+9=11
1+1=2
Output: 2
"""

def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n