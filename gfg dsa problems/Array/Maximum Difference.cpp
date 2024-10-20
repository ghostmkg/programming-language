//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    /*You are required to complete this method */
    int findMaxDiff(vector<int> &arr) {
        // Your code here
        int n = arr.size();
        stack<int> s;
        vector<int> left(n, 0);
        vector<int> right(n, 0);
        s.push(arr[0]);
        for(int i = 1; i< n; i++){
            while(!s.empty() && s.top() >= arr[i]){
                s.pop();
                
            }
            if(!s.empty()){
                left[i] = s.top();
            }
            s.push(arr[i]);
        }
        while (!s.empty()) {
            s.pop(); 
        }
        s.push(arr[n-1]);
        for(int i = n-2; i>=0 ; i--){
            while(!s.empty() && s.top() >= arr[i]){
                s.pop();
            }
            if(!s.empty()){
                right[i] = s.top();
            }
            s.push(arr[i]);
        }
        int maxi = INT_MIN;
        for (int i = 0; i<n; i++){
            maxi = max(maxi, abs(left[i]-right[i]));
        }
        return maxi;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    cin.ignore();

    while (t--) {
        string input;
        int num;
        vector<int> arr;

        getline(cin, input);
        stringstream s2(input);
        while (s2 >> num) {
            arr.push_back(num);
        }

        Solution ob;
        cout << ob.findMaxDiff(arr) << endl;
    }
    return 0;
}

// } Driver Code Ends
