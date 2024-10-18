//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    // Function to reverse words in a given string.
    string reverseWords(string str) {
        // code here
        reverse(str.begin(), str.end());
    
    int a = 0, b = 0;
  
    while (b < str.size()) {
        
        while (b < str.size() && str[b] != '.') {
            b++;
        }
        
        reverse(str.begin() + a, str.begin() + b);
        
        b++;
        a = b;
    }
    
    return str;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        Solution obj;
        cout << obj.reverseWords(s) << endl;
    }
}
// } Driver Code Ends
