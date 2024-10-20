//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int maxLength(string& str) {
        // code here
        int n=str.length();
        vector<bool> seen(n, false);
        stack<int> st;
        int i=0;
        while(i<n) {
            if(str[i]=='(') {
                st.push(i);
            }else {
                if(!st.empty() && str[st.top()]=='(' ) {
                    int tem = st.top(); 
                    st.pop();           
                    seen[tem] = true;   
                    seen[i] = true;
                }
            }
            i++;
        }

        int cnt=0;
        int ans=0;
        for(int j=0;j<n;j++) {
            if(seen[j]==true) cnt++;
            else cnt=0;
            ans=max(ans, cnt);
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        string S;
        cin >> S;

        Solution ob;
        cout << ob.maxLength(S) << "\n";
    }
    return 0;
}
// } Driver Code Ends
