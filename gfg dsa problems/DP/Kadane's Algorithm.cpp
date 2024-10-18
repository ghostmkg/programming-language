//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++
class Solution {
  public:
    // Function to find the sum of contiguous subarray with maximum sum.
    int maxSubarraySum(vector<int> &arr) {
        // code here...
        int n =arr.size();
        int maxi =INT_MIN;
        vector<int> dp(n+1);
        dp[0] =0;
        for(int i =1;i<=n;i++){
            maxi=max(maxi,arr[i-1]);
            if(dp[i -1] +arr[i-1]>=0){
                dp[i] =dp[i -1] +arr[i -1];
            }else{
                dp[i] =0;
            }
        }
        if(maxi <= 0){
            return maxi;
        }
        return *max_element(dp.begin(),dp.end());
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore(); // To discard any leftover newline characters
    while (t--)   // while testcases exist
    {
        vector<int> arr;
        string input;
        getline(cin, input); // Read the entire line for the array elements
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        cout << ob.maxSubarraySum(arr) << endl;
    }
}
// } Driver Code Ends
