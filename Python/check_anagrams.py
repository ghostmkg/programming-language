"""
Problem:
Two strings are anagrams if one is a rearrangement of the other.

Example:
Input: "listen", "silent" → Output: True
"""

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)