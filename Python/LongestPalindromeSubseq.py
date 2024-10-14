class Solution:
    def check(self, s, dp, i, j):
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s[i] == s[j]:
            if i != j:
                dp[i][j] = 2 + self.check(s, dp, i + 1, j - 1)
            else:
                dp[i][j] = 1 + self.check(s, dp, i + 1, j - 1)
        else:
            dp[i][j] = max(self.check(s, dp, i, j - 1), self.check(s, dp, i + 1, j))
        
        return dp[i][j]

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return self.check(s, dp, 0, n - 1)

# Example test cases
solution = Solution()

# Test case 1
s1 = "bbbab"
output1 = solution.longestPalindromeSubseq(s1)
print(f"Output for '{s1}': {output1}")  # Expected output: 4

# Test case 2
s2 = "cbbd"
output2 = solution.longestPalindromeSubseq(s2)
print(f"Output for '{s2}': {output2}")  # Expected output: 2
