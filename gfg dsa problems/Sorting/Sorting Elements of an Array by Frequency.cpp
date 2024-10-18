//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
    // Complete this function
    // Function to sort the array according to frequency of elements
    static bool func(pair<int, int> &a,pair<int, int> &b){

        if(a.second>b.second) return true;

        else if(a.second<b.second) return false;

        else return a.first<b.first;

    }


    vector<int> sortByFreq(vector<int>& arr) {

        // Your code here

        unordered_map<int, int> mm;

        vector<pair<int, int>> vec;

        vector<int> ans;

        for(auto x:arr)mm[x]++;

        for(auto x:arr)vec.push_back({x,mm[x]});

        sort(vec.begin(),vec.end(),func);

        for(auto x:vec)ans.push_back(x.first);

        return ans;
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
        Solution obj;
        vector<int> v;
        v = obj.sortByFreq(arr);
        for (int i : v)
            cout << i << " ";
        cout << endl;
    }

    return 0;
}

// } Driver Code Ends
