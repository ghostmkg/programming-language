"""
Advanced String Algorithms Implementation
=========================================

Comprehensive string algorithms including pattern matching,
palindromes, anagrams, and string manipulation techniques.

Author: Hacktoberfest 2025 Contributor
"""

from typing import List, Dict
from collections import defaultdict, Counter


class StringAlgorithms:
    """Collection of advanced string algorithms"""
    
    @staticmethod
    def kmp_search(text: str, pattern: str) -> List[int]:
        """
        Knuth-Morris-Pratt Pattern Matching
        
        Time: O(n + m) where n = len(text), m = len(pattern)
        Space: O(m)
        
        Returns: List of starting indices where pattern is found
        """
        if not pattern or not text:
            return []
        
        # Build LPS (Longest Prefix Suffix) array
        def build_lps(pattern):
            lps = [0] * len(pattern)
            length = 0
            i = 1
            
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        lps = build_lps(pattern)
        result = []
        i = j = 0
        
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
                
            if j == len(pattern):
                result.append(i - j)
                j = lps[j - 1]
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return result
    
    @staticmethod
    def rabin_karp(text: str, pattern: str) -> List[int]:
        """
        Rabin-Karp String Matching (using rolling hash)
        
        Time: O(n + m) average, O(nm) worst
        Space: O(1)
        """
        if not pattern or not text:
            return []
        
        n, m = len(text), len(pattern)
        if m > n:
            return []
        
        d = 256  # Number of characters
        q = 101  # Prime number
        result = []
        
        # Calculate hash values
        p_hash = 0  # Pattern hash
        t_hash = 0  # Text window hash
        h = pow(d, m - 1, q)
        
        # Initial hash
        for i in range(m):
            p_hash = (d * p_hash + ord(pattern[i])) % q
            t_hash = (d * t_hash + ord(text[i])) % q
        
        # Slide pattern over text
        for i in range(n - m + 1):
            if p_hash == t_hash:
                # Hash match - verify character by character
                if text[i:i+m] == pattern:
                    result.append(i)
            
            # Calculate hash for next window
            if i < n - m:
                t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
                if t_hash < 0:
                    t_hash += q
        
        return result
    
    @staticmethod
    def longest_palindrome_substring(s: str) -> str:
        """
        Find longest palindromic substring
        
        Time: O(n^2)
        Space: O(1)
        """
        if not s:
            return ""
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        longest = ""
        for i in range(len(s)):
            # Odd length palindromes
            palindrome1 = expand_around_center(i, i)
            # Even length palindromes
            palindrome2 = expand_around_center(i, i + 1)
            
            current = palindrome1 if len(palindrome1) > len(palindrome2) else palindrome2
            if len(current) > len(longest):
                longest = current
        
        return longest
    
    @staticmethod
    def manacher_algorithm(s: str) -> str:
        """
        Manacher's Algorithm for longest palindrome
        
        Time: O(n)
        Space: O(n)
        """
        if not s:
            return ""
        
        # Transform string
        t = '#'.join(f"^{s}$")
        n = len(t)
        p = [0] * n
        center = right = 0
        
        for i in range(1, n - 1):
            if i < right:
                p[i] = min(right - i, p[2 * center - i])
            
            # Expand around center i
            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1
            
            # Update center and right boundary
            if i + p[i] > right:
                center, right = i, i + p[i]
        
        # Find longest palindrome
        max_len, center_index = max((length, i) for i, length in enumerate(p))
        start = (center_index - max_len) // 2
        return s[start:start + max_len]
    
    @staticmethod
    def group_anagrams(words: List[str]) -> List[List[str]]:
        """
        Group anagrams together
        
        Time: O(n * k log k) where k is max word length
        Space: O(n * k)
        """
        anagram_map = defaultdict(list)
        
        for word in words:
            # Sort characters to create key
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())
    
    @staticmethod
    def is_rotation(s1: str, s2: str) -> bool:
        """
        Check if s2 is rotation of s1
        
        Time: O(n)
        Space: O(n)
        """
        return len(s1) == len(s2) and s2 in (s1 + s1)
    
    @staticmethod
    def z_algorithm(s: str) -> List[int]:
        """
        Z Algorithm for pattern matching
        
        Time: O(n)
        Space: O(n)
        
        Returns: Z-array where z[i] is length of longest substring
                 starting from s[i] which is also prefix of s
        """
        n = len(s)
        z = [0] * n
        z[0] = n
        
        l, r = 0, 0
        for i in range(1, n):
            if i > r:
                l = r = i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1
            else:
                k = i - l
                if z[k] < r - i + 1:
                    z[i] = z[k]
                else:
                    l = i
                    while r < n and s[r - l] == s[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1
        
        return z
    
    @staticmethod
    def word_break(s: str, word_dict: List[str]) -> bool:
        """
        Word Break Problem using DP
        
        Time: O(n^2)
        Space: O(n)
        """
        word_set = set(word_dict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[len(s)]


# Demonstration
def demonstrate_string_algorithms():
    print("=" * 70)
    print("STRING ALGORITHMS DEMONSTRATION")
    print("=" * 70)
    
    algo = StringAlgorithms()
    
    # KMP Pattern Matching
    print("\n1. KMP PATTERN MATCHING")
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = algo.kmp_search(text, pattern)
    print(f"   Text: {text}")
    print(f"   Pattern: {pattern}")
    print(f"   Matches at indices: {matches}")
    
    # Rabin-Karp
    print("\n2. RABIN-KARP ALGORITHM")
    matches = algo.rabin_karp(text, "ABAB")
    print(f"   Pattern 'ABAB' found at: {matches}")
    
    # Longest Palindrome
    print("\n3. LONGEST PALINDROMIC SUBSTRING")
    s = "babad"
    print(f"   String: {s}")
    print(f"   Longest palindrome: {algo.longest_palindrome_substring(s)}")
    
    # Manacher's Algorithm
    print("\n4. MANACHER'S ALGORITHM")
    s = "babcbabcbaccba"
    print(f"   String: {s}")
    print(f"   Longest palindrome: {algo.manacher_algorithm(s)}")
    
    # Group Anagrams
    print("\n5. GROUP ANAGRAMS")
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groups = algo.group_anagrams(words)
    print(f"   Words: {words}")
    print(f"   Anagram groups: {groups}")
    
    # String Rotation
    print("\n6. STRING ROTATION")
    s1, s2 = "waterbottle", "erbottlewat"
    print(f"   Is '{s2}' rotation of '{s1}'? {algo.is_rotation(s1, s2)}")
    
    # Z Algorithm
    print("\n7. Z ALGORITHM")
    s = "aabxaabxcaabxaabxay"
    z = algo.z_algorithm(s)
    print(f"   String: {s}")
    print(f"   Z-array: {z[:10]}...")
    
    # Word Break
    print("\n8. WORD BREAK")
    s = "leetcode"
    word_dict = ["leet", "code"]
    print(f"   String: {s}")
    print(f"   Dictionary: {word_dict}")
    print(f"   Can break: {algo.word_break(s, word_dict)}")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    demonstrate_string_algorithms()
