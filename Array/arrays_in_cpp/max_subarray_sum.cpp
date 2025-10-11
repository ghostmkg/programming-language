#include <iostream>
#include <vector>
using namespace std;

int maxSubarraySum(const vector<int>& arr) {
    int maxSum = arr[0], currSum = arr[0];
    for (int i = 1; i < arr.size(); i++) {
        currSum = max(arr[i], currSum + arr[i]);
        maxSum = max(maxSum, currSum);
    }
    return maxSum;
}

int main() {
    vector<int> arr;
    int n;

    cout<<"\nenter the size of the array :\n";
    cin>>n;

    cout<<"\nenter the array elements :\n";
    for(int i=0; i<n; i++){
        int ele;
        cin>>ele;

        arr.push_back(ele);
    }
    
    cout << "Maximum subarray sum: " << maxSubarraySum(arr);
    return 0;
}
