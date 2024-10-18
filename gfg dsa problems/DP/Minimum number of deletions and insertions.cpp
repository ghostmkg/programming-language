//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
		

	public:
	
    int minOperations(string str1, string str2) { 
	    int n = str1.size(), m = str2.size();
	    vector<vector<int>> dp(n+1, vector<int>(m+1));
	    
	    for(int i = 0; i <= n; i++) 
	        dp[i][0] = i;
	    for(int j = 0; j <= m; j++)
	        dp[0][j] = j;
	        
	    for(int i = 1; i <= n; i++) 
	        for(int j = 1; j <= m; j++) 
	            if(str1[i-1] == str2[j-1]) dp[i][j] = dp[i-1][j-1];
	            else dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1]); 

	    return dp[n][m];
	}
	
};

//{ Driver Code Starts.
int main() 
{
   	
   
   	int t;
    cin >> t;
    while (t--)
    {
        string s1, s2;
        cin >> s1 >> s2;

	    Solution ob;
	    cout << ob.minOperations(s1, s2) << "\n";
	     
    }
    return 0;
}


// } Driver Code Ends
