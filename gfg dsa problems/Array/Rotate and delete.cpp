//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int rotateDelete(vector<int> &arr) {
        // Your code here
        deque<int>dq(arr.begin(),arr.end());
        int k=1;
        int n=arr.size();
        
            while(k<=dq.size()){
                int a=dq[dq.size()-1];
                dq.pop_back();
                dq.push_front(a);
                int b=dq.size()-k;
                dq.erase(dq.begin()+b);
                k++;
            }
                   
                   return dq[0];
    }
};


//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution obj;
        int res = obj.rotateDelete(arr);
        cout << res << endl;
        // string tl;
        // getline(cin, tl);
    }
    return 0;
}

// } Driver Code Ends
