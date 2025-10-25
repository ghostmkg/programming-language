/**
 * Dynamic Programming Algorithms Implementation
 * ==============================================
 * 
 * Comprehensive collection of classic dynamic programming problems
 * with optimal solutions, detailed explanations, and complexity analysis.
 * 
 * Problems Implemented:
 * - Fibonacci (multiple approaches)
 * - Longest Common Subsequence (LCS)
 * - Longest Increasing Subsequence (LIS)
 * - 0/1 Knapsack Problem
 * - Coin Change Problem
 * - Edit Distance (Levenshtein)
 * - Matrix Chain Multiplication
 * - Rod Cutting Problem
 * - Palindrome Partitioning
 * - Egg Drop Problem
 * 
 * Author: Hacktoberfest 2025 Contributor
 */

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <climits>
#include <cstring>

using namespace std;

class DynamicProgramming {
public:
    /**
     * Fibonacci Number - Multiple Approaches
     * 
     * 1. Naive Recursion: O(2^n) time, O(n) space
     * 2. Memoization: O(n) time, O(n) space
     * 3. Tabulation: O(n) time, O(n) space
     * 4. Space Optimized: O(n) time, O(1) space
     */
    
    // Memoization approach
    static long long fibMemo(int n, vector<long long>& memo) {
        if (n <= 1) return n;
        if (memo[n] != -1) return memo[n];
        return memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo);
    }
    
    static long long fibonacci(int n) {
        vector<long long> memo(n + 1, -1);
        return fibMemo(n, memo);
    }
    
    // Space optimized tabulation
    static long long fibOptimized(int n) {
        if (n <= 1) return n;
        long long prev2 = 0, prev1 = 1;
        for (int i = 2; i <= n; i++) {
            long long curr = prev1 + prev2;
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
    
    /**
     * Longest Common Subsequence (LCS)
     * 
     * Time Complexity: O(m * n)
     * Space Complexity: O(m * n)
     * 
     * Returns length of LCS of two strings
     */
    static int longestCommonSubsequence(const string& text1, const string& text2) {
        int m = text1.length();
        int n = text2.length();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1[i-1] == text2[j-1]) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        
        return dp[m][n];
    }
    
    // Get actual LCS string
    static string getLCS(const string& text1, const string& text2) {
        int m = text1.length();
        int n = text2.length();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
        // Fill DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1[i-1] == text2[j-1]) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        
        // Backtrack to find LCS
        string lcs = "";
        int i = m, j = n;
        while (i > 0 && j > 0) {
            if (text1[i-1] == text2[j-1]) {
                lcs = text1[i-1] + lcs;
                i--;
                j--;
            } else if (dp[i-1][j] > dp[i][j-1]) {
                i--;
            } else {
                j--;
            }
        }
        
        return lcs;
    }
    
    /**
     * Longest Increasing Subsequence (LIS)
     * 
     * Time Complexity: O(n^2) - DP solution
     * Space Complexity: O(n)
     */
    static int longestIncreasingSubsequence(const vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        
        vector<int> dp(n, 1);
        int maxLen = 1;
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            maxLen = max(maxLen, dp[i]);
        }
        
        return maxLen;
    }
    
    /**
     * 0/1 Knapsack Problem
     * 
     * Time Complexity: O(n * W) where W is capacity
     * Space Complexity: O(n * W)
     * 
     * Returns maximum value that can be obtained
     */
    static int knapsack(const vector<int>& weights, const vector<int>& values, int capacity) {
        int n = weights.size();
        vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));
        
        for (int i = 1; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                if (weights[i-1] <= w) {
                    dp[i][w] = max(dp[i-1][w], 
                                   values[i-1] + dp[i-1][w - weights[i-1]]);
                } else {
                    dp[i][w] = dp[i-1][w];
                }
            }
        }
        
        return dp[n][capacity];
    }
    
    /**
     * Coin Change - Minimum Coins
     * 
     * Time Complexity: O(n * amount)
     * Space Complexity: O(amount)
     */
    static int coinChange(const vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i && dp[i - coin] != INT_MAX) {
                    dp[i] = min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        
        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
    
    /**
     * Edit Distance (Levenshtein Distance)
     * 
     * Time Complexity: O(m * n)
     * Space Complexity: O(m * n)
     */
    static int editDistance(const string& word1, const string& word2) {
        int m = word1.length();
        int n = word2.length();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));
        
        // Initialize base cases
        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;
        
        // Fill DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i-1] == word2[j-1]) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    dp[i][j] = 1 + min({dp[i-1][j],     // Delete
                                        dp[i][j-1],     // Insert
                                        dp[i-1][j-1]}); // Replace
                }
            }
        }
        
        return dp[m][n];
    }
    
    /**
     * Matrix Chain Multiplication
     * 
     * Time Complexity: O(n^3)
     * Space Complexity: O(n^2)
     * 
     * Returns minimum number of multiplications needed
     */
    static int matrixChainMultiplication(const vector<int>& dimensions) {
        int n = dimensions.size() - 1;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        // len is chain length
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i < n - len + 1; i++) {
                int j = i + len - 1;
                dp[i][j] = INT_MAX;
                
                for (int k = i; k < j; k++) {
                    int cost = dp[i][k] + dp[k+1][j] + 
                              dimensions[i] * dimensions[k+1] * dimensions[j+1];
                    dp[i][j] = min(dp[i][j], cost);
                }
            }
        }
        
        return dp[0][n-1];
    }
    
    /**
     * Rod Cutting Problem
     * 
     * Time Complexity: O(n^2)
     * Space Complexity: O(n)
     */
    static int rodCutting(const vector<int>& prices, int length) {
        vector<int> dp(length + 1, 0);
        
        for (int i = 1; i <= length; i++) {
            for (int j = 1; j <= i; j++) {
                if (j <= prices.size()) {
                    dp[i] = max(dp[i], prices[j-1] + dp[i-j]);
                }
            }
        }
        
        return dp[length];
    }
    
    /**
     * Palindrome Partitioning - Minimum Cuts
     * 
     * Time Complexity: O(n^2)
     * Space Complexity: O(n^2)
     */
    static int minPalindromePartitioning(const string& s) {
        int n = s.length();
        vector<vector<bool>> isPalin(n, vector<bool>(n, false));
        vector<int> cuts(n, 0);
        
        // Build palindrome table
        for (int len = 1; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                if (s[i] == s[j] && (len <= 2 || isPalin[i+1][j-1])) {
                    isPalin[i][j] = true;
                }
            }
        }
        
        // Calculate minimum cuts
        for (int i = 0; i < n; i++) {
            if (isPalin[0][i]) {
                cuts[i] = 0;
            } else {
                cuts[i] = INT_MAX;
                for (int j = 0; j < i; j++) {
                    if (isPalin[j+1][i]) {
                        cuts[i] = min(cuts[i], cuts[j] + 1);
                    }
                }
            }
        }
        
        return cuts[n-1];
    }
    
    /**
     * Egg Drop Problem
     * 
     * Time Complexity: O(n * k^2) where n is eggs, k is floors
     * Space Complexity: O(n * k)
     */
    static int eggDrop(int eggs, int floors) {
        vector<vector<int>> dp(eggs + 1, vector<int>(floors + 1, 0));
        
        // Base cases
        for (int i = 1; i <= eggs; i++) {
            dp[i][0] = 0;
            dp[i][1] = 1;
        }
        
        for (int j = 1; j <= floors; j++) {
            dp[1][j] = j;
        }
        
        // Fill DP table
        for (int i = 2; i <= eggs; i++) {
            for (int j = 2; j <= floors; j++) {
                dp[i][j] = INT_MAX;
                for (int x = 1; x <= j; x++) {
                    int worst = 1 + max(dp[i-1][x-1], dp[i][j-x]);
                    dp[i][j] = min(dp[i][j], worst);
                }
            }
        }
        
        return dp[eggs][floors];
    }
};

// Demonstration
void demonstrateDynamicProgramming() {
    cout << string(70, '=') << endl;
    cout << "DYNAMIC PROGRAMMING ALGORITHMS DEMONSTRATION" << endl;
    cout << string(70, '=') << endl;
    
    cout << "\n1. FIBONACCI" << endl;
    cout << string(70, '-') << endl;
    cout << "   Fib(10) = " << DynamicProgramming::fibonacci(10) << endl;
    cout << "   Fib(20) = " << DynamicProgramming::fibOptimized(20) << endl;
    
    cout << "\n2. LONGEST COMMON SUBSEQUENCE" << endl;
    cout << string(70, '-') << endl;
    string s1 = "ABCDGH", s2 = "AEDFHR";
    cout << "   LCS(\"" << s1 << "\", \"" << s2 << "\") = " 
         << DynamicProgramming::longestCommonSubsequence(s1, s2) << endl;
    cout << "   LCS String: " << DynamicProgramming::getLCS(s1, s2) << endl;
    
    cout << "\n3. LONGEST INCREASING SUBSEQUENCE" << endl;
    cout << string(70, '-') << endl;
    vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << "   Array: [10, 9, 2, 5, 3, 7, 101, 18]" << endl;
    cout << "   LIS Length = " 
         << DynamicProgramming::longestIncreasingSubsequence(nums) << endl;
    
    cout << "\n4. 0/1 KNAPSACK" << endl;
    cout << string(70, '-') << endl;
    vector<int> weights = {1, 3, 4, 5};
    vector<int> values = {1, 4, 5, 7};
    int capacity = 7;
    cout << "   Capacity = " << capacity << endl;
    cout << "   Maximum Value = " 
         << DynamicProgramming::knapsack(weights, values, capacity) << endl;
    
    cout << "\n5. COIN CHANGE" << endl;
    cout << string(70, '-') << endl;
    vector<int> coins = {1, 2, 5};
    int amount = 11;
    cout << "   Coins: [1, 2, 5], Amount = " << amount << endl;
    cout << "   Minimum Coins = " 
         << DynamicProgramming::coinChange(coins, amount) << endl;
    
    cout << "\n6. EDIT DISTANCE" << endl;
    cout << string(70, '-') << endl;
    string word1 = "horse", word2 = "ros";
    cout << "   Word1: \"" << word1 << "\", Word2: \"" << word2 << "\"" << endl;
    cout << "   Edit Distance = " 
         << DynamicProgramming::editDistance(word1, word2) << endl;
    
    cout << "\n7. MATRIX CHAIN MULTIPLICATION" << endl;
    cout << string(70, '-') << endl;
    vector<int> dimensions = {10, 20, 30, 40, 30};
    cout << "   Minimum Multiplications = " 
         << DynamicProgramming::matrixChainMultiplication(dimensions) << endl;
    
    cout << "\n8. ROD CUTTING" << endl;
    cout << string(70, '-') << endl;
    vector<int> prices = {1, 5, 8, 9, 10, 17, 17, 20};
    cout << "   Rod Length = 8" << endl;
    cout << "   Maximum Revenue = " 
         << DynamicProgramming::rodCutting(prices, 8) << endl;
    
    cout << "\n9. EGG DROP PROBLEM" << endl;
    cout << string(70, '-') << endl;
    cout << "   Eggs = 2, Floors = 10" << endl;
    cout << "   Minimum Trials = " 
         << DynamicProgramming::eggDrop(2, 10) << endl;
    
    cout << "\n" << string(70, '=') << endl;
}

int main() {
    demonstrateDynamicProgramming();
    return 0;
}
