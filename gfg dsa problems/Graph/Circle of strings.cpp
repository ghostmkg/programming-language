//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function Template for C++

class Solution {
  public:
    int isCircle(vector<string> &arr) {
        // code here
        int n = arr.size();
        vector<int> vis(n,0),indegree(26,0),outdegree(26,0);
        unordered_map<char,vector<int>> mm;
        queue<int> q;
        for(int i=0;i<n;i++){
            indegree[arr[i][0]-'a']++;
            outdegree[arr[i].back()-'a']++;
            mm[arr[i][0]].push_back(i);
        }
        for(auto x:mm){
            if(indegree[x.first-'a']!=outdegree[x.first-'a'])return 0;
        }
        q.push(0);
        vis[0]=1;
        int ans = 1;
        while(!q.empty()){
            int index = q.front();
            q.pop();
            for(auto x:mm[arr[index].back()]){
                if(!vis[x]){
                    ans++;
                    vis[x]=1;
                    q.push(x);
                }
            }
        }
        return ans==n;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        vector<string> A;
        string s;

        for (int i = 0; i < N; i++) {
            cin >> s;
            A.push_back(s);
        }

        Solution ob;
        cout << ob.isCircle(A) << endl;
    }
    return 0;
}
// } Driver Code Ends
