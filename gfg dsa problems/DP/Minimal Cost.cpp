int n = arr.size();
        vector<int> dp(n, INT_MAX); 
        dp[0] = 0; 

        for (int i = 0; i < n; ++i) {
            for (int jump = 1; jump <= k && i + jump < n; ++jump) {
                dp[i + jump] = min(dp[i + jump], dp[i] + abs(arr[i] - arr[i + jump]));
            }
        }

        return dp[n - 1]; 
