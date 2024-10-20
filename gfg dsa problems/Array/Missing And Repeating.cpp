//{ Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


// } Driver Code Ends
class Solution {
  public:
    vector<int> findTwoElement(vector<int>& arr) {
        // code here
        int n=arr.size();
        vector<int>ans;
        vector<int>visited(n+1,0);
        visited[0]=1;
        for(int i=0;i<n;i++){
            if(visited[arr[i]]==0){
                visited[arr[i]]=1;
            }else if(visited[arr[i]]==1){
                ans.push_back(arr[i]);
            }
        }
        
        for(int i=0;i<n+1;i++){
            if(visited[i]==0){
                ans.push_back(i);
                break;
            }
        }
        
        return ans;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        auto ans = ob.findTwoElement(a);
        cout << ans[0] << " " << ans[1] << "\n";
    }
    return 0;
}
// } Driver Code Ends
