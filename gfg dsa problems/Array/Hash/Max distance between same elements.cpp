//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    int maxDistance(vector<int> &arr) {
        // Code here
        unordered_map<int,int> first ;
        unordered_map<int ,int> last;
        
        for(int i = 0; i < arr.size(); i++){
            
            if(first.find(arr[i]) != first.end()){
                continue;
            }
            first[arr[i]] =i;
            
        }
        
        for(int i =0; i< arr.size(); i++){
            last[arr[i]] = i;
        }
        
        int ans =0;
        for(auto it : first ){
            ans = max(ans  , last[it.first] - it.second);
        }
        return ans;
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);

        stringstream s1(input);
        int num;
        while (s1 >> num) {
            arr.push_back(num);
        }

        Solution ob;
        cout << ob.maxDistance(arr) << endl;
    }
    return 0;
}
// } Driver Code Ends
