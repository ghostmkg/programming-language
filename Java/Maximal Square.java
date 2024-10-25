class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        int rows = matrix.length;
        int cols = matrix[0].length;
        int maxSide = 0;

        // Create a DP array to store the size of the largest square ending at each position
        int[][] dp = new int[rows][cols];

        // Fill the DP array
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (matrix[i][j] == '1') {
                    if (i == 0 || j == 0) {
                        // If we're at the first row or first column, the largest square ending here is just 1
                        dp[i][j] = 1;
                    } else {
                        // Otherwise, calculate the size of the square based on the surrounding squares
                        dp[i][j] = Math.min(Math.min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
                    }
                    // Update the maximum side length found
                    maxSide = Math.max(maxSide, dp[i][j]);
                }
            }
        }

        // The area of the largest square is side length squared
        return maxSide * maxSide;
    }
}