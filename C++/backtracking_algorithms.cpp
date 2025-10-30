/**
 * Backtracking Algorithms Implementation
 * ======================================
 * 
 * Classic backtracking problems including N-Queens, Sudoku Solver,
 * Permutations, Combinations, and Subset Sum.
 * 
 * Author: Hacktoberfest 2025 Contributor
 */

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class BacktrackingAlgorithms {
public:
    /**
     * N-Queens Problem
     * Time: O(N!)
     * Space: O(N)
     */
    static vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> solutions;
        vector<string> board(n, string(n, '.'));
        
        backtrackQueens(0, board, solutions);
        return solutions;
    }
    
private:
    static void backtrackQueens(int row, vector<string>& board, 
                               vector<vector<string>>& solutions) {
        if (row == board.size()) {
            solutions.push_back(board);
            return;
        }
        
        for (int col = 0; col < board.size(); col++) {
            if (isValidQueen(board, row, col)) {
                board[row][col] = 'Q';
                backtrackQueens(row + 1, board, solutions);
                board[row][col] = '.';
            }
        }
    }
    
    static bool isValidQueen(const vector<string>& board, int row, int col) {
        // Check column
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') return false;
        }
        
        // Check diagonal (top-left)
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') return false;
        }
        
        // Check diagonal (top-right)
        for (int i = row - 1, j = col + 1; i >= 0 && j < board.size(); i--, j++) {
            if (board[i][j] == 'Q') return false;
        }
        
        return true;
    }

public:
    /**
     * Sudoku Solver
     * Time: O(9^(n*n))
     * Space: O(n*n)
     */
    static bool solveSudoku(vector<vector<char>>& board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col] == '.') {
                    for (char num = '1'; num <= '9'; num++) {
                        if (isValidSudoku(board, row, col, num)) {
                            board[row][col] = num;
                            
                            if (solveSudoku(board)) return true;
                            
                            board[row][col] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    
private:
    static bool isValidSudoku(const vector<vector<char>>& board, 
                             int row, int col, char num) {
        // Check row
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == num) return false;
        }
        
        // Check column
        for (int i = 0; i < 9; i++) {
            if (board[i][col] == num) return false;
        }
        
        // Check 3x3 box
        int boxRow = (row / 3) * 3;
        int boxCol = (col / 3) * 3;
        
        for (int i = boxRow; i < boxRow + 3; i++) {
            for (int j = boxCol; j < boxCol + 3; j++) {
                if (board[i][j] == num) return false;
            }
        }
        
        return true;
    }

public:
    /**
     * Generate all permutations
     * Time: O(n * n!)
     * Space: O(n)
     */
    static vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrackPermute(nums, 0, result);
        return result;
    }
    
private:
    static void backtrackPermute(vector<int>& nums, int start, 
                                vector<vector<int>>& result) {
        if (start == nums.size()) {
            result.push_back(nums);
            return;
        }
        
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);
            backtrackPermute(nums, start + 1, result);
            swap(nums[start], nums[i]);
        }
    }

public:
    /**
     * Generate all combinations of size k
     * Time: O(C(n, k))
     * Space: O(k)
     */
    static vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> result;
        vector<int> current;
        
        backtrackCombine(1, n, k, current, result);
        return result;
    }
    
private:
    static void backtrackCombine(int start, int n, int k, 
                                 vector<int>& current, 
                                 vector<vector<int>>& result) {
        if (current.size() == k) {
            result.push_back(current);
            return;
        }
        
        for (int i = start; i <= n; i++) {
            current.push_back(i);
            backtrackCombine(i + 1, n, k, current, result);
            current.pop_back();
        }
    }

public:
    /**
     * Subset Sum Problem
     * Time: O(2^n)
     * Space: O(n)
     */
    static vector<vector<int>> subsetSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        vector<int> current;
        sort(nums.begin(), nums.end());
        
        backtrackSubsetSum(nums, 0, target, current, result);
        return result;
    }
    
private:
    static void backtrackSubsetSum(const vector<int>& nums, int start, 
                                   int target, vector<int>& current, 
                                   vector<vector<int>>& result) {
        if (target == 0) {
            result.push_back(current);
            return;
        }
        
        if (target < 0) return;
        
        for (int i = start; i < nums.size(); i++) {
            current.push_back(nums[i]);
            backtrackSubsetSum(nums, i + 1, target - nums[i], current, result);
            current.pop_back();
        }
    }

public:
    /**
     * Generate all subsets (power set)
     * Time: O(2^n)
     * Space: O(n)
     */
    static vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        
        backtrackSubsets(nums, 0, current, result);
        return result;
    }
    
private:
    static void backtrackSubsets(const vector<int>& nums, int start, 
                                vector<int>& current, 
                                vector<vector<int>>& result) {
        result.push_back(current);
        
        for (int i = start; i < nums.size(); i++) {
            current.push_back(nums[i]);
            backtrackSubsets(nums, i + 1, current, result);
            current.pop_back();
        }
    }

public:
    /**
     * Word Search in grid
     * Time: O(m * n * 4^L) where L is word length
     * Space: O(L)
     */
    static bool wordSearch(vector<vector<char>>& board, string word) {
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (backtrackWordSearch(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
    
private:
    static bool backtrackWordSearch(vector<vector<char>>& board, 
                                    const string& word, 
                                    int row, int col, int index) {
        if (index == word.length()) return true;
        
        if (row < 0 || row >= board.size() || 
            col < 0 || col >= board[0].size() || 
            board[row][col] != word[index]) {
            return false;
        }
        
        char temp = board[row][col];
        board[row][col] = '#';  // Mark as visited
        
        bool found = backtrackWordSearch(board, word, row + 1, col, index + 1) ||
                     backtrackWordSearch(board, word, row - 1, col, index + 1) ||
                     backtrackWordSearch(board, word, row, col + 1, index + 1) ||
                     backtrackWordSearch(board, word, row, col - 1, index + 1);
        
        board[row][col] = temp;  // Restore
        return found;
    }
};

// Demonstration
void demonstrateBacktracking() {
    cout << string(70, '=') << endl;
    cout << "BACKTRACKING ALGORITHMS DEMONSTRATION" << endl;
    cout << string(70, '=') << endl;
    
    // N-Queens
    cout << "\n1. N-QUEENS (N=4)" << endl;
    auto queens = BacktrackingAlgorithms::solveNQueens(4);
    cout << "   Number of solutions: " << queens.size() << endl;
    cout << "   First solution:" << endl;
    for (const auto& row : queens[0]) {
        cout << "   " << row << endl;
    }
    
    // Permutations
    cout << "\n2. PERMUTATIONS" << endl;
    vector<int> nums = {1, 2, 3};
    auto perms = BacktrackingAlgorithms::permute(nums);
    cout << "   Permutations of [1,2,3]:" << endl;
    for (const auto& perm : perms) {
        cout << "   [";
        for (int i = 0; i < perm.size(); i++) {
            cout << perm[i] << (i < perm.size() - 1 ? ", " : "");
        }
        cout << "]" << endl;
    }
    
    // Combinations
    cout << "\n3. COMBINATIONS" << endl;
    auto combs = BacktrackingAlgorithms::combine(4, 2);
    cout << "   C(4, 2) = " << combs.size() << " combinations" << endl;
    
    // Subsets
    cout << "\n4. POWER SET" << endl;
    vector<int> set = {1, 2, 3};
    auto subsets = BacktrackingAlgorithms::subsets(set);
    cout << "   Subsets of [1,2,3]: " << subsets.size() << " subsets" << endl;
    
    // Subset Sum
    cout << "\n5. SUBSET SUM" << endl;
    vector<int> arr = {2, 3, 5, 7};
    auto sums = BacktrackingAlgorithms::subsetSum(arr, 10);
    cout << "   Subsets that sum to 10:" << endl;
    for (const auto& subset : sums) {
        cout << "   [";
        for (int i = 0; i < subset.size(); i++) {
            cout << subset[i] << (i < subset.size() - 1 ? ", " : "");
        }
        cout << "]" << endl;
    }
    
    cout << "\n" << string(70, '=') << endl;
}

int main() {
    demonstrateBacktracking();
    return 0;
}
