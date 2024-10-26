public class Solution {

    public static int rearrangeSticks(int n, int k) {
        final int MOD = 1_000_000_007;

        // dp[i][j] represents the number of arrangements for i sticks with j sticks visible from the left
        long[][] dp = new long[n + 1][k + 1];

        dp[0][0] = 1;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                // Current stick is placed at the end
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % MOD;

                // Current stick is not placed at the end
                dp[i][j] = (dp[i][j] + (dp[i - 1][j] * (i - 1)) % MOD) % MOD;
            }
        }

        return (int) dp[n][k];
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(rearrangeSticks(3, 2)); // Output: 3
        System.out.println(rearrangeSticks(5, 5)); // Output: 1
        System.out.println(rearrangeSticks(20, 11)); // Output: 647427950
    }
}