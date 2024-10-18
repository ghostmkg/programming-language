//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++

class Solution {
  public:
    int lps(string str) {
        // Your code goes here
        int n = str.length();
        vector<int> p(n, 0);
    
        for (int i = 1; i < n; ++i) {
            int j = p[i - 1];
            while (j > 0 && str[j] != str[i]) {
                j = p[j - 1];
            }
            if (str[j] == str[i]) {
                ++j;
            }
            p[i] = j;
        }
        return p[n - 1];

    }
};

//{ Driver Code Starts.

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        string str;
        cin >> str;

        Solution ob;

        cout << ob.lps(str) << "\n";
    }

    return 0;
}

// } Driver Code Ends
